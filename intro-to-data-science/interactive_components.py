"""
Interactive Components for Data Science Bootcamp
================================================
Interactive widgets and UI components for the notebook
"""

import ipywidgets as widgets
from IPython.display import display, HTML, clear_output, Javascript
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from typing import Dict, List, Any, Callable
import time
import random


class InteractiveQuiz:
    """Create interactive multiple-choice quizzes"""
    
    def __init__(self, title: str = "Knowledge Check"):
        self.title = title
        self.questions = []
        self.user_answers = {}
        self.score = 0
        
    def add_question(self, question: str, options: List[str], correct_index: int, explanation: str = ""):
        """Add a question to the quiz"""
        self.questions.append({
            'question': question,
            'options': options,
            'correct': correct_index,
            'explanation': explanation
        })
    
    def create_quiz(self):
        """Create the interactive quiz widget"""
        quiz_container = widgets.VBox()
        question_widgets = []
        
        for i, q in enumerate(self.questions):
            # Create radio buttons for options
            radio = widgets.RadioButtons(
                options=q['options'],
                description='',
                disabled=False,
                layout=widgets.Layout(width='auto')
            )
            
            # Create question label
            question_label = widgets.HTML(
                value=f"<b>Question {i+1}:</b> {q['question']}"
            )
            
            # Feedback area
            feedback = widgets.HTML(value="")
            
            # Store widgets
            question_widgets.append({
                'radio': radio,
                'feedback': feedback,
                'correct': q['correct'],
                'explanation': q['explanation']
            })
            
            # Add to container
            quiz_container.children += (
                question_label,
                radio,
                feedback,
                widgets.HTML(value="<hr>")
            )
        
        # Submit button
        submit_btn = widgets.Button(
            description='Submit Quiz',
            button_style='primary',
            icon='check'
        )
        
        # Score display
        score_display = widgets.HTML(value="")
        
        def on_submit(btn):
            total = len(self.questions)
            correct = 0
            
            for i, qw in enumerate(question_widgets):
                selected = qw['radio'].index
                if selected is not None:
                    if selected == qw['correct']:
                        correct += 1
                        qw['feedback'].value = '<span style="color:green">✅ Correct!</span>'
                    else:
                        qw['feedback'].value = f'<span style="color:red">❌ Incorrect. {qw["explanation"]}</span>'
            
            self.score = (correct / total) * 100
            score_display.value = f"""
            <div style="padding:10px; background:#f0f0f0; border-radius:5px; margin-top:10px;">
                <h3>Quiz Results</h3>
                <p>Score: <b>{correct}/{total}</b> ({self.score:.0f}%)</p>
                {self._get_feedback_message(self.score)}
            </div>
            """
        
        submit_btn.on_click(on_submit)
        
        quiz_container.children += (submit_btn, score_display)
        
        return quiz_container
    
    def _get_feedback_message(self, score: float) -> str:
        """Get feedback message based on score"""
        if score >= 90:
            return "🌟 Excellent! You've mastered this topic!"
        elif score >= 70:
            return "👍 Good job! You have a solid understanding."
        elif score >= 50:
            return "📚 Not bad, but review the material to improve."
        else:
            return "💪 Keep practicing! Review the concepts and try again."


class CodePlayground:
    """Interactive code playground with instant feedback"""
    
    def __init__(self, initial_code: str = "", exercise_name: str = "Practice"):
        self.initial_code = initial_code
        self.exercise_name = exercise_name
        
    def create_playground(self, validator: Callable = None):
        """Create interactive code editor with run button"""
        
        # Code editor
        code_editor = widgets.Textarea(
            value=self.initial_code,
            placeholder='Type your Python code here...',
            description='Code:',
            disabled=False,
            layout=widgets.Layout(width='100%', height='200px')
        )
        
        # Output area
        output_area = widgets.Output(
            layout=widgets.Layout(width='100%', height='150px', border='1px solid #ddd')
        )
        
        # Run button
        run_btn = widgets.Button(
            description='Run Code',
            button_style='success',
            icon='play'
        )
        
        # Clear button
        clear_btn = widgets.Button(
            description='Clear',
            button_style='warning',
            icon='trash'
        )
        
        # Reset button
        reset_btn = widgets.Button(
            description='Reset',
            button_style='info',
            icon='refresh'
        )
        
        def run_code(btn):
            code = code_editor.value
            with output_area:
                clear_output()
                try:
                    # Execute the code
                    exec_globals = {}
                    exec(code, exec_globals)
                    
                    # Run validator if provided
                    if validator:
                        result = validator(code, exec_globals)
                        if result:
                            print(f"\n✅ {result}")
                except Exception as e:
                    print(f"❌ Error: {e}")
        
        def clear_output_area(btn):
            with output_area:
                clear_output()
        
        def reset_code(btn):
            code_editor.value = self.initial_code
            with output_area:
                clear_output()
        
        run_btn.on_click(run_code)
        clear_btn.on_click(clear_output_area)
        reset_btn.on_click(reset_code)
        
        # Layout
        buttons = widgets.HBox([run_btn, clear_btn, reset_btn])
        
        container = widgets.VBox([
            widgets.HTML(f"<h4>🖥️ {self.exercise_name}</h4>"),
            code_editor,
            buttons,
            widgets.HTML("<b>Output:</b>"),
            output_area
        ])
        
        return container


class DataExplorer:
    """Interactive data exploration widget"""
    
    def __init__(self, df: pd.DataFrame, name: str = "Dataset"):
        self.df = df
        self.name = name
        
    def create_explorer(self):
        """Create interactive data explorer"""
        
        # Tab widget for different views
        tab = widgets.Tab()
        
        # Data preview
        preview_output = widgets.Output()
        with preview_output:
            display(HTML(f"<h4>Dataset: {self.name}</h4>"))
            display(self.df.head(10))
        
        # Statistics
        stats_output = widgets.Output()
        with stats_output:
            display(HTML("<h4>Statistical Summary</h4>"))
            display(self.df.describe())
        
        # Info
        info_output = widgets.Output()
        with info_output:
            display(HTML("<h4>Dataset Information</h4>"))
            print(f"Shape: {self.df.shape}")
            print(f"Columns: {list(self.df.columns)}")
            print(f"\nData Types:")
            print(self.df.dtypes)
            print(f"\nMissing Values:")
            print(self.df.isnull().sum())
        
        # Interactive filter
        filter_container = self._create_filter_widget()
        
        # Visualization
        viz_container = self._create_visualization_widget()
        
        # Set up tabs
        tab.children = [preview_output, stats_output, info_output, filter_container, viz_container]
        tab.set_title(0, 'Preview')
        tab.set_title(1, 'Statistics')
        tab.set_title(2, 'Info')
        tab.set_title(3, 'Filter')
        tab.set_title(4, 'Visualize')
        
        return tab
    
    def _create_filter_widget(self):
        """Create interactive filter widget"""
        filter_output = widgets.Output()
        
        # Column selector
        columns = list(self.df.columns)
        column_select = widgets.Dropdown(
            options=columns,
            description='Column:',
            disabled=False,
        )
        
        # Value input
        value_input = widgets.Text(
            placeholder='Enter filter value',
            description='Value:',
            disabled=False,
        )
        
        # Filter button
        filter_btn = widgets.Button(
            description='Apply Filter',
            button_style='primary',
            icon='filter'
        )
        
        # Results area
        results_output = widgets.Output()
        
        def apply_filter(btn):
            with results_output:
                clear_output()
                try:
                    col = column_select.value
                    val = value_input.value
                    
                    # Try to convert to appropriate type
                    if self.df[col].dtype in ['int64', 'float64']:
                        val = float(val)
                        filtered = self.df[self.df[col] == val]
                    else:
                        filtered = self.df[self.df[col].astype(str).str.contains(val, case=False)]
                    
                    display(HTML(f"<b>Filtered Results ({len(filtered)} rows):</b>"))
                    display(filtered.head(20))
                except Exception as e:
                    print(f"Error: {e}")
        
        filter_btn.on_click(apply_filter)
        
        container = widgets.VBox([
            widgets.HTML("<h4>Interactive Filter</h4>"),
            column_select,
            value_input,
            filter_btn,
            results_output
        ])
        
        return container
    
    def _create_visualization_widget(self):
        """Create interactive visualization widget"""
        viz_output = widgets.Output()
        
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns.tolist()
        categorical_cols = self.df.select_dtypes(include=['object']).columns.tolist()
        
        # Chart type selector
        chart_type = widgets.Dropdown(
            options=['histogram', 'scatter', 'bar', 'box', 'correlation'],
            description='Chart Type:',
            disabled=False,
        )
        
        # Column selectors
        x_column = widgets.Dropdown(
            options=numeric_cols + categorical_cols,
            description='X-axis:',
            disabled=False,
        )
        
        y_column = widgets.Dropdown(
            options=['None'] + numeric_cols,
            value='None',
            description='Y-axis:',
            disabled=False,
        )
        
        # Plot button
        plot_btn = widgets.Button(
            description='Create Plot',
            button_style='success',
            icon='chart-bar'
        )
        
        # Plot area
        plot_output = widgets.Output()
        
        def create_plot(btn):
            with plot_output:
                clear_output()
                try:
                    chart = chart_type.value
                    x = x_column.value
                    y = y_column.value if y_column.value != 'None' else None
                    
                    if chart == 'histogram':
                        fig = px.histogram(self.df, x=x, title=f'Histogram of {x}')
                    elif chart == 'scatter' and y:
                        fig = px.scatter(self.df, x=x, y=y, title=f'{x} vs {y}')
                    elif chart == 'bar':
                        if x in categorical_cols:
                            counts = self.df[x].value_counts()
                            fig = px.bar(x=counts.index, y=counts.values, 
                                       labels={'x': x, 'y': 'Count'},
                                       title=f'Bar Chart of {x}')
                        else:
                            fig = px.histogram(self.df, x=x, title=f'Bar Chart of {x}')
                    elif chart == 'box':
                        fig = px.box(self.df, y=x, title=f'Box Plot of {x}')
                    elif chart == 'correlation':
                        corr = self.df[numeric_cols].corr()
                        fig = px.imshow(corr, title='Correlation Matrix',
                                      labels=dict(color="Correlation"))
                    else:
                        print("Please select appropriate columns for this chart type")
                        return
                    
                    fig.show()
                except Exception as e:
                    print(f"Error creating plot: {e}")
        
        plot_btn.on_click(create_plot)
        
        container = widgets.VBox([
            widgets.HTML("<h4>Interactive Visualization</h4>"),
            chart_type,
            x_column,
            y_column,
            plot_btn,
            plot_output
        ])
        
        return container


class ProgressTracker:
    """Track and display student progress through the notebook"""
    
    def __init__(self, total_modules: int = 6):
        self.total_modules = total_modules
        self.completed_modules = []
        self.current_module = 0
        
    def create_tracker(self):
        """Create progress tracker widget"""
        progress = widgets.FloatProgress(
            value=0,
            min=0,
            max=self.total_modules,
            description='Progress:',
            bar_style='',
            style={'bar_color': 'green'},
            orientation='horizontal'
        )
        
        progress_label = widgets.HTML(value="")
        
        # Module checkboxes
        module_checks = []
        for i in range(self.total_modules):
            check = widgets.Checkbox(
                value=False,
                description=f'Module {i}',
                disabled=False,
                indent=False
            )
            module_checks.append(check)
        
        def update_progress(change):
            completed = sum(1 for check in module_checks if check.value)
            progress.value = completed
            percentage = (completed / self.total_modules) * 100
            progress_label.value = f"<b>{percentage:.0f}% Complete</b> ({completed}/{self.total_modules} modules)"
            
            if completed == self.total_modules:
                progress.bar_style = 'success'
                progress_label.value += " 🎉 <b>Congratulations! You've completed the course!</b>"
        
        for check in module_checks:
            check.observe(update_progress, names='value')
        
        container = widgets.VBox([
            widgets.HTML("<h3>📊 Your Progress</h3>"),
            progress,
            progress_label,
            widgets.HTML("<b>Completed Modules:</b>"),
            widgets.HBox(module_checks)
        ])
        
        return container


class InteractiveDashboard:
    """Create interactive dashboards"""
    
    @staticmethod
    def create_realtime_counter():
        """Create a real-time data generation counter"""
        output = widgets.Output()
        
        def update_counter():
            # Simulate real-time data generation
            gb_per_second = 2.5
            start_time = time.time()
            
            for _ in range(10):
                with output:
                    clear_output(wait=True)
                    elapsed = time.time() - start_time
                    data_generated = gb_per_second * elapsed
                    
                    display(HTML(f"""
                    <div style="text-align:center; padding:20px; background:#f8f9fa; border-radius:10px;">
                        <h2>🌍 Global Data Generation</h2>
                        <h1 style="color:#007bff; font-size:48px;">{data_generated:.1f} GB</h1>
                        <p>Generated in the last {elapsed:.0f} seconds</p>
                        <p style="color:#6c757d;">That's {gb_per_second} GB per second worldwide!</p>
                    </div>
                    """))
                    
                time.sleep(1)
        
        # Start button
        start_btn = widgets.Button(
            description='Start Counter',
            button_style='primary',
            icon='play'
        )
        
        start_btn.on_click(lambda x: update_counter())
        
        return widgets.VBox([start_btn, output])
    
    @staticmethod
    def create_skill_matcher():
        """Create an interactive skill matching game"""
        skills = {
            'Python': 'Programming language for data science',
            'Pandas': 'Data manipulation library',
            'NumPy': 'Numerical computing library',
            'Matplotlib': 'Data visualization library',
            'Scikit-learn': 'Machine learning library',
            'SQL': 'Database query language'
        }
        
        # Create dropdowns for matching
        skill_options = list(skills.keys())
        description_options = list(skills.values())
        
        matches = []
        for skill in skill_options:
            skill_label = widgets.HTML(value=f"<b>{skill}:</b>")
            desc_dropdown = widgets.Dropdown(
                options=['Select...'] + description_options,
                value='Select...',
                layout=widgets.Layout(width='300px')
            )
            matches.append((skill, desc_dropdown))
        
        # Check button
        check_btn = widgets.Button(
            description='Check Answers',
            button_style='primary',
            icon='check'
        )
        
        # Results display
        results = widgets.HTML(value="")
        
        def check_matches(btn):
            correct = 0
            total = len(matches)
            
            for skill, dropdown in matches:
                if dropdown.value == skills[skill]:
                    correct += 1
            
            score = (correct / total) * 100
            if score == 100:
                msg = "🎉 Perfect! You got all matches correct!"
            elif score >= 70:
                msg = f"👍 Good job! You got {correct}/{total} correct."
            else:
                msg = f"Keep trying! You got {correct}/{total} correct."
            
            results.value = f"""
            <div style="padding:10px; background:#e7f3ff; border-left:4px solid #007bff; margin-top:10px;">
                {msg}
            </div>
            """
        
        check_btn.on_click(check_matches)
        
        # Layout
        match_widgets = []
        for skill, dropdown in matches:
            match_widgets.append(widgets.HBox([
                widgets.HTML(value=f"<b style='width:100px; display:inline-block;'>{skill}:</b>"),
                dropdown
            ]))
        
        container = widgets.VBox([
            widgets.HTML("<h3>🎯 Match the Skill to its Description</h3>"),
            *match_widgets,
            check_btn,
            results
        ])
        
        return container


def create_welcome_message(student_name: str = "Data Scientist"):
    """Create personalized welcome message"""
    return HTML(f"""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                color: white; padding: 30px; border-radius: 10px; text-align: center;">
        <h1>🚀 Welcome to Data Science Bootcamp, {student_name}!</h1>
        <p style="font-size: 18px;">Your journey into the world of data begins now...</p>
        <p>📊 Analyze • 🤖 Predict • 💡 Innovate</p>
    </div>
    """)


def create_module_header(module_num: int, title: str, duration: str):
    """Create styled module header"""
    return HTML(f"""
    <div style="background: #f8f9fa; border-left: 5px solid #007bff; 
                padding: 20px; margin: 20px 0; border-radius: 5px;">
        <h2>Module {module_num}: {title}</h2>
        <p>⏱️ Duration: {duration}</p>
    </div>
    """)


def create_tip_box(tip: str, tip_type: str = "info"):
    """Create styled tip/warning box"""
    colors = {
        'info': '#17a2b8',
        'success': '#28a745',
        'warning': '#ffc107',
        'danger': '#dc3545'
    }
    
    icons = {
        'info': 'ℹ️',
        'success': '✅',
        'warning': '⚠️',
        'danger': '❌'
    }
    
    return HTML(f"""
    <div style="background: {colors[tip_type]}20; border-left: 4px solid {colors[tip_type]}; 
                padding: 15px; margin: 15px 0; border-radius: 5px;">
        <p style="margin: 0;"><b>{icons[tip_type]} Tip:</b> {tip}</p>
    </div>
    """)


def create_code_cell_with_hints(code: str, hints: List[str]):
    """Create a code cell with progressive hints"""
    hint_widgets = []
    
    for i, hint in enumerate(hints):
        hint_btn = widgets.Button(
            description=f'Hint {i+1}',
            button_style='info',
            icon='lightbulb-o'
        )
        
        hint_text = widgets.HTML(value="")
        
        def show_hint(btn, h=hint, ht=hint_text):
            ht.value = f"<p style='background:#fff3cd; padding:10px; border-radius:5px;'>💡 {h}</p>"
        
        hint_btn.on_click(show_hint)
        hint_widgets.append(widgets.VBox([hint_btn, hint_text]))
    
    return widgets.VBox([
        widgets.HTML(f"<pre style='background:#f4f4f4; padding:10px;'>{code}</pre>"),
        widgets.HTML("<b>Need help? Click the hints below:</b>"),
        widgets.HBox(hint_widgets)
    ])


class DataScienceMagicShow:
    """Interactive 'magic show' demo to hook students from the start"""
    
    def __init__(self):
        self.predictions = []
        self.class_data = {}
    
    def create_magic_demo(self):
        """Create the opening magic show widget"""
        title = widgets.HTML(value="""
        <div style="background: linear-gradient(135deg, #6C63FF 0%, #4ECDC4 100%); 
                    color: white; padding: 20px; border-radius: 10px; text-align: center; margin: 20px 0;">
            <h1>🎩 Welcome to the Data Science Magic Show! ✨</h1>
            <p style="font-size: 18px;">Let me predict something about our class using the power of data...</p>
        </div>
        """)
        
        # Student input form
        age_input = widgets.IntSlider(value=25, min=18, max=65, description='Your Age:')
        experience_input = widgets.Dropdown(
            options=['Complete Beginner', 'Some Experience', 'Intermediate', 'Advanced'],
            value='Complete Beginner',
            description='Experience:'
        )
        motivation_input = widgets.Dropdown(
            options=['Career Change', 'Skill Enhancement', 'Academic', 'Curiosity'],
            value='Curiosity',
            description='Motivation:'
        )
        
        submit_btn = widgets.Button(
            description='Submit & See Magic! 🎪',
            button_style='primary',
            layout=widgets.Layout(width='200px')
        )
        
        results_area = widgets.Output()
        
        def perform_magic(btn):
            age = age_input.value
            exp = experience_input.value
            motivation = motivation_input.value
            
            # Store class data
            if 'ages' not in self.class_data:
                self.class_data = {'ages': [], 'experiences': [], 'motivations': []}
            
            self.class_data['ages'].append(age)
            self.class_data['experiences'].append(exp)
            self.class_data['motivations'].append(motivation)
            
            with results_area:
                clear_output()
                
                # "Magic" predictions based on patterns
                avg_age = np.mean(self.class_data['ages'])
                most_common_exp = max(set(self.class_data['experiences']), 
                                    key=self.class_data['experiences'].count)
                
                magic_insights = [
                    f"🔮 I predict our class average age is around {avg_age:.0f} years!",
                    f"✨ Most of you are '{most_common_exp}' - perfect for this bootcamp!",
                    f"🌟 Based on the data patterns, this class will be 87% successful!",
                    f"🎯 I sense great potential for {motivation.lower()} in your future!"
                ]
                
                display(HTML("""
                <div style="background: #f8f9fa; padding: 20px; border-radius: 10px; margin: 10px 0;">
                    <h3>🎭 The Magic Reveals...</h3>
                    <ul>
                """ + ''.join([f"<li>{insight}</li>" for insight in magic_insights]) + """
                    </ul>
                    <p style="color: #6C63FF; font-weight: bold;">This is the power of data science - finding patterns and insights!</p>
                </div>
                """))
                
                # Show simple visualization
                if len(self.class_data['ages']) > 1:
                    fig = px.histogram(x=self.class_data['ages'], 
                                     title="Live Class Demographics",
                                     labels={'x': 'Age', 'y': 'Count'})
                    fig.update_layout(height=300, showlegend=False)
                    fig.show()
        
        submit_btn.on_click(perform_magic)
        
        form = widgets.VBox([
            widgets.HTML("<h4>📝 Tell me about yourself (anonymous data):</h4>"),
            age_input,
            experience_input, 
            motivation_input,
            submit_btn
        ], layout=widgets.Layout(padding='20px', border='2px solid #6C63FF', border_radius='10px'))
        
        return widgets.VBox([title, form, results_area])


class LivePolling:
    """Real-time polling system for class engagement"""
    
    def __init__(self, question: str, options: List[str]):
        self.question = question
        self.options = options
        self.votes = {option: 0 for option in options}
        
    def create_poll(self):
        """Create interactive poll widget"""
        poll_title = widgets.HTML(value=f"""
        <div style="background: #6C63FF; color: white; padding: 15px; border-radius: 10px; margin: 10px 0;">
            <h3>📊 Live Poll: {self.question}</h3>
        </div>
        """)
        
        # Voting buttons
        vote_buttons = []
        for option in self.options:
            btn = widgets.Button(
                description=option,
                button_style='info',
                layout=widgets.Layout(width='400px', margin='5px')
            )
            vote_buttons.append(btn)
        
        results_area = widgets.Output()
        
        def vote(btn):
            option = btn.description
            self.votes[option] += 1
            btn.button_style = 'success'
            btn.description = f"{option} ✓"
            btn.disabled = True
            
            # Disable other buttons
            for other_btn in vote_buttons:
                if other_btn != btn:
                    other_btn.disabled = True
            
            self.show_results(results_area)
        
        for btn in vote_buttons:
            btn.on_click(vote)
        
        return widgets.VBox([
            poll_title,
            widgets.HTML("<p>Click your choice:</p>"),
            widgets.VBox(vote_buttons),
            results_area
        ])
    
    def show_results(self, output_area):
        """Display poll results"""
        with output_area:
            clear_output()
            total_votes = sum(self.votes.values())
            if total_votes > 0:
                results_html = "<h4>📈 Live Results:</h4><ul>"
                for option, count in self.votes.items():
                    percentage = (count / total_votes) * 100
                    bar = "█" * int(percentage / 5)  # Visual bar
                    results_html += f"<li>{option}: {count} votes ({percentage:.1f}%) {bar}</li>"
                results_html += "</ul>"
                display(HTML(results_html))


class GamificationEngine:
    """Manage points, badges, and achievements throughout the session"""
    
    def __init__(self, student_name: str = "Data Scientist"):
        self.student_name = student_name
        self.total_points = 0
        self.badges = []
        self.achievements = []
        
    def award_points(self, points: int, reason: str = ""):
        """Award points with celebration"""
        self.total_points += points
        
        celebration = f"""
        <div style="background: linear-gradient(45deg, #FFB800, #FF6B6B); 
                    color: white; padding: 15px; border-radius: 10px; 
                    text-align: center; margin: 10px 0; 
                    animation: pulse 2s infinite;">
            <h3>🎉 +{points} Points! 🎉</h3>
            <p>{reason}</p>
            <p><strong>Total Score: {self.total_points}</strong></p>
        </div>
        """
        
        display(HTML(celebration))
        return self.total_points
    
    def unlock_badge(self, badge_name: str, description: str):
        """Unlock achievement badge"""
        if badge_name not in self.badges:
            self.badges.append(badge_name)
            
            badge_html = f"""
            <div style="background: #00D084; color: white; padding: 20px; 
                        border-radius: 10px; text-align: center; margin: 15px 0;
                        border: 3px solid gold;">
                <h2>🏆 BADGE UNLOCKED! 🏆</h2>
                <h3>✨ {badge_name} ✨</h3>
                <p>{description}</p>
                <p style="font-size: 12px;">Badge {len(self.badges)} of 10</p>
            </div>
            """
            
            display(HTML(badge_html))
    
    def show_progress_dashboard(self):
        """Display current progress and achievements"""
        dashboard = f"""
        <div style="background: #f8f9fa; padding: 20px; border-radius: 10px; 
                    border: 2px solid #6C63FF; margin: 20px 0;">
            <h3>📊 {self.student_name}'s Progress Dashboard</h3>
            <div style="display: flex; justify-content: space-around; margin: 20px 0;">
                <div style="text-align: center;">
                    <h2 style="color: #6C63FF;">{self.total_points}</h2>
                    <p>Points Earned</p>
                </div>
                <div style="text-align: center;">
                    <h2 style="color: #00D084;">{len(self.badges)}</h2>
                    <p>Badges Unlocked</p>
                </div>
                <div style="text-align: center;">
                    <h2 style="color: #FFB800;">{len(self.achievements)}</h2>
                    <p>Achievements</p>
                </div>
            </div>
            <div>
                <h4>🏆 Your Badges:</h4>
                <p>{'🎖️ '.join(self.badges) if self.badges else 'No badges yet - keep going!'}</p>
            </div>
        </div>
        """
        
        display(HTML(dashboard))
    
    def get_total_score(self):
        """Return the total score earned"""
        return self.total_points
    
    def get_badges(self):
        """Return list of earned badges"""
        return self.badges


class InteractiveDemo:
    """Create hands-on demo experiences"""
    
    @staticmethod
    def create_fraud_detective_game(transactions_data):
        """Interactive fraud detection game"""
        # Sample suspicious transactions
        suspicious = [
            {"amount": 9999.99, "time": "3:00 AM", "location": "Foreign", "merchant": "Unknown"},
            {"amount": 25.50, "time": "2:00 PM", "location": "Local", "merchant": "Coffee Shop"},
            {"amount": 5000.00, "time": "11:59 PM", "location": "Foreign", "merchant": "Electronics"},
            {"amount": 12.99, "time": "6:00 PM", "location": "Local", "merchant": "Restaurant"}
        ]
        
        game_title = widgets.HTML(value="""
        <div style="background: #FF5E5B; color: white; padding: 20px; border-radius: 10px; text-align: center;">
            <h2>🕵️ Fraud Detective Challenge 🕵️</h2>
            <p>You're a bank's fraud analyst. Which transactions look suspicious?</p>
        </div>
        """)
        
        # Create checkboxes for each transaction
        checkboxes = []
        for i, trans in enumerate(suspicious):
            desc = f"${trans['amount']} at {trans['time']} - {trans['location']} - {trans['merchant']}"
            checkbox = widgets.Checkbox(
                value=False,
                description=desc,
                layout=widgets.Layout(width='500px')
            )
            checkboxes.append((checkbox, i in [0, 2]))  # 0 and 2 are the fraudulent ones
        
        submit_btn = widgets.Button(
            description='Submit Analysis 🔍',
            button_style='danger'
        )
        
        results_area = widgets.Output()
        
        def check_fraud_detection(btn):
            with results_area:
                clear_output()
                correct = 0
                total_fraud = 2
                
                for checkbox, is_fraud in checkboxes:
                    if checkbox.value == is_fraud:
                        correct += 1
                
                accuracy = (correct / len(checkboxes)) * 100
                
                if accuracy == 100:
                    message = "🎉 Perfect! You caught all the fraudsters and protected innocent customers!"
                    points = 50
                elif accuracy >= 75:
                    message = "👍 Good detective work! You caught most of the suspicious activity."
                    points = 30
                else:
                    message = "🔍 Keep practicing! Fraud detection is tricky but you're learning."
                    points = 10
                
                result_html = f"""
                <div style="background: #e7f3ff; padding: 20px; border-radius: 10px; margin: 10px 0;">
                    <h3>🎯 Analysis Results</h3>
                    <p>{message}</p>
                    <p><strong>Accuracy: {accuracy:.0f}%</strong></p>
                    <p>Points Earned: {points}</p>
                    <h4>🔍 The Real Fraudsters:</h4>
                    <ul>
                        <li>$9,999.99 at 3:00 AM from Foreign location ❌</li>
                        <li>$5,000.00 at 11:59 PM from Foreign Electronics ❌</li>
                    </ul>
                    <p><em>High amounts + unusual times + foreign locations = Red flags!</em></p>
                </div>
                """
                
                display(HTML(result_html))
        
        submit_btn.on_click(check_fraud_detection)
        
        transaction_widgets = [widgets.HTML("<h4>📊 Select the suspicious transactions:</h4>")]
        for checkbox, _ in checkboxes:
            transaction_widgets.append(checkbox)
        
        return widgets.VBox([
            game_title,
            *transaction_widgets,
            submit_btn,
            results_area
        ])
    
    @staticmethod
    def create_data_science_workflow_demo():
        """Interactive workflow demonstration"""
        steps = [
            {"name": "🤔 Ask Questions", "description": "What problem are we solving?", "example": "Why do customers churn?"},
            {"name": "📊 Collect Data", "description": "Gather relevant information", "example": "Customer behavior, demographics, usage patterns"},
            {"name": "🧹 Clean Data", "description": "Remove errors and inconsistencies", "example": "Handle missing values, remove duplicates"},
            {"name": "🔍 Explore Data", "description": "Discover patterns and insights", "example": "Create visualizations, calculate statistics"},
            {"name": "🤖 Build Models", "description": "Create predictive algorithms", "example": "Train machine learning models"},
            {"name": "📈 Interpret Results", "description": "Extract meaningful insights", "example": "Model shows price sensitivity matters most"}
        ]
        
        current_step = 0
        
        title = widgets.HTML(value="""
        <div style="background: #6C63FF; color: white; padding: 20px; border-radius: 10px; text-align: center;">
            <h2>🔄 Interactive Data Science Workflow</h2>
            <p>Click through each step to see the process in action!</p>
        </div>
        """)
        
        step_display = widgets.HTML()
        next_btn = widgets.Button(description="Next Step ➡️", button_style='primary')
        reset_btn = widgets.Button(description="🔄 Start Over", button_style='info')
        
        def update_step_display():
            if current_step < len(steps):
                step = steps[current_step]
                step_display.value = f"""
                <div style="background: #f8f9fa; padding: 25px; border-radius: 10px; 
                            border-left: 5px solid #00D084; margin: 20px 0;">
                    <h3>Step {current_step + 1}: {step['name']}</h3>
                    <p><strong>{step['description']}</strong></p>
                    <p style="color: #6c757d;"><em>Example: {step['example']}</em></p>
                    <div style="background: #e7f3ff; padding: 10px; border-radius: 5px; margin-top: 10px;">
                        Progress: {current_step + 1}/{len(steps)} steps completed
                    </div>
                </div>
                """
            else:
                step_display.value = """
                <div style="background: #00D084; color: white; padding: 25px; 
                            border-radius: 10px; text-align: center; margin: 20px 0;">
                    <h2>🎉 Workflow Complete! 🎉</h2>
                    <p>You've learned the complete data science process!</p>
                    <p>Now you're ready to tackle real-world problems!</p>
                </div>
                """
                next_btn.disabled = True
        
        def next_step(btn):
            nonlocal current_step
            current_step += 1
            update_step_display()
        
        def reset_workflow(btn):
            nonlocal current_step
            current_step = 0
            next_btn.disabled = False
            update_step_display()
        
        next_btn.on_click(next_step)
        reset_btn.on_click(reset_workflow)
        
        # Initialize display
        update_step_display()
        
        controls = widgets.HBox([next_btn, reset_btn])
        
        return widgets.VBox([title, step_display, controls])