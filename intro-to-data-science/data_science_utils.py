"""
Data Science Bootcamp - Utility Functions
==========================================
Helper functions for the interactive Data Science introduction notebook
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from typing import Dict, List, Tuple, Any
import random
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')


class DataScienceKit:
    """Personal Data Science Toolkit for students"""
    
    def __init__(self, student_name: str = "Student"):
        self.student_name = student_name
        self.completed_exercises = []
        self.score = 0
        self.start_time = datetime.now()
        
    def add_achievement(self, exercise_name: str, points: int = 10):
        """Track student progress"""
        self.completed_exercises.append(exercise_name)
        self.score += points
        return f"🎉 Great job! You earned {points} points. Total score: {self.score}"
    
    def get_progress(self):
        """Display student progress"""
        duration = datetime.now() - self.start_time
        return {
            'student': self.student_name,
            'exercises_completed': len(self.completed_exercises),
            'total_score': self.score,
            'time_spent': str(duration).split('.')[0]
        }
    
    def create_progress_bar(self, current: int, total: int):
        """Create visual progress bar"""
        percentage = (current / total) * 100
        filled = int(percentage / 5)
        bar = '█' * filled + '░' * (20 - filled)
        return f"Progress: [{bar}] {percentage:.1f}%"


class InteractiveVisualizer:
    """Create interactive visualizations for the notebook"""
    
    @staticmethod
    def create_word_cloud_data(words: List[str], frequencies: List[int]):
        """Generate data for word cloud visualization"""
        df = pd.DataFrame({
            'word': words,
            'frequency': frequencies,
            'size': [f * 3 for f in frequencies]
        })
        return df
    
    @staticmethod
    def create_timeline(events: Dict[str, str]):
        """Create interactive timeline"""
        fig = go.Figure()
        
        years = list(events.keys())
        descriptions = list(events.values())
        
        fig.add_trace(go.Scatter(
            x=years,
            y=[1] * len(years),
            mode='markers+text',
            marker=dict(size=15, color='royalblue'),
            text=descriptions,
            textposition='top center',
            hovertemplate='<b>%{x}</b><br>%{text}<extra></extra>'
        ))
        
        fig.update_layout(
            title="Evolution of Data Science",
            xaxis_title="Year",
            yaxis=dict(visible=False),
            height=400,
            hovermode='closest'
        )
        
        return fig
    
    @staticmethod
    def create_industry_impact_chart(industries: Dict[str, float]):
        """Create industry impact visualization"""
        df = pd.DataFrame({
            'Industry': list(industries.keys()),
            'Impact': list(industries.values())
        })
        
        fig = px.bar(df, x='Industry', y='Impact',
                     title='Data Science Impact by Industry',
                     color='Impact',
                     color_continuous_scale='Viridis')
        return fig
    
    @staticmethod
    def create_skill_radar(skills: Dict[str, int]):
        """Create radar chart for skills assessment"""
        categories = list(skills.keys())
        values = list(skills.values())
        
        fig = go.Figure(data=go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            name='Current Skills'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 10]
                )),
            showlegend=False,
            title="Your Data Science Skills Assessment"
        )
        
        return fig


class DataGenerator:
    """Generate sample datasets for exercises"""
    
    @staticmethod
    def generate_customer_data(n_customers: int = 1000):
        """Generate synthetic customer data"""
        np.random.seed(42)
        
        data = {
            'customer_id': range(1, n_customers + 1),
            'age': np.random.randint(18, 70, n_customers),
            'gender': np.random.choice(['M', 'F', 'Other'], n_customers, p=[0.45, 0.45, 0.1]),
            'income': np.random.normal(50000, 20000, n_customers).round(0),
            'spending_score': np.random.randint(1, 100, n_customers),
            'membership_years': np.random.randint(0, 10, n_customers),
            'purchase_frequency': np.random.poisson(5, n_customers),
            'preferred_category': np.random.choice(
                ['Electronics', 'Clothing', 'Food', 'Books', 'Sports'],
                n_customers
            )
        }
        
        df = pd.DataFrame(data)
        df['income'] = df['income'].clip(lower=15000)
        df['customer_segment'] = pd.cut(df['spending_score'], 
                                       bins=[0, 33, 66, 100],
                                       labels=['Low', 'Medium', 'High'])
        
        return df
    
    @staticmethod
    def generate_patient_data(n_patients: int = 500):
        """Generate synthetic healthcare data"""
        np.random.seed(42)
        
        data = {
            'patient_id': [f'P{i:04d}' for i in range(1, n_patients + 1)],
            'age': np.random.randint(18, 85, n_patients),
            'bmi': np.random.normal(26, 5, n_patients).round(1),
            'blood_pressure': np.random.randint(90, 160, n_patients),
            'glucose_level': np.random.normal(100, 20, n_patients).round(0),
            'smoker': np.random.choice([0, 1], n_patients, p=[0.7, 0.3]),
            'exercise_hours': np.random.exponential(2, n_patients).round(1),
            'readmitted': np.random.choice([0, 1], n_patients, p=[0.75, 0.25]),
            'days_in_hospital': np.random.poisson(3, n_patients)
        }
        
        df = pd.DataFrame(data)
        df['risk_score'] = (
            (df['age'] > 60).astype(int) +
            (df['bmi'] > 30).astype(int) +
            (df['blood_pressure'] > 140).astype(int) +
            df['smoker'] +
            (df['exercise_hours'] < 1).astype(int)
        )
        
        return df
    
    @staticmethod
    def generate_transaction_data(n_transactions: int = 10000):
        """Generate synthetic financial transaction data"""
        np.random.seed(42)
        
        start_date = datetime.now() - timedelta(days=365)
        dates = [start_date + timedelta(days=random.randint(0, 365)) 
                for _ in range(n_transactions)]
        
        data = {
            'transaction_id': [f'T{i:06d}' for i in range(1, n_transactions + 1)],
            'date': dates,
            'amount': np.random.exponential(100, n_transactions).round(2),
            'merchant_category': np.random.choice(
                ['Grocery', 'Gas', 'Restaurant', 'Online', 'Entertainment', 'Other'],
                n_transactions,
                p=[0.3, 0.15, 0.2, 0.15, 0.1, 0.1]
            ),
            'location': np.random.choice(
                ['Local', 'National', 'International'],
                n_transactions,
                p=[0.7, 0.25, 0.05]
            ),
            'payment_method': np.random.choice(
                ['Credit', 'Debit', 'Cash', 'Digital'],
                n_transactions,
                p=[0.4, 0.3, 0.1, 0.2]
            )
        }
        
        df = pd.DataFrame(data)
        
        # Add fraud labels (rare events)
        fraud_indices = np.random.choice(df.index, size=int(0.002 * len(df)), replace=False)
        df['is_fraud'] = 0
        df.loc[fraud_indices, 'is_fraud'] = 1
        
        # Fraudulent transactions tend to be larger
        df.loc[df['is_fraud'] == 1, 'amount'] *= np.random.uniform(2, 5, sum(df['is_fraud']))
        
        return df


class ExerciseValidator:
    """Validate student exercise submissions"""
    
    @staticmethod
    def check_answer(student_answer: Any, correct_answer: Any, tolerance: float = 0.01):
        """Check if student's answer is correct"""
        if isinstance(correct_answer, (int, float)):
            return abs(student_answer - correct_answer) < tolerance
        else:
            return student_answer == correct_answer
    
    @staticmethod
    def validate_code(code_string: str, required_elements: List[str]):
        """Check if code contains required elements"""
        missing = [elem for elem in required_elements if elem not in code_string]
        if not missing:
            return True, "✅ Great! Your code contains all required elements."
        else:
            return False, f"❌ Missing elements: {', '.join(missing)}"
    
    @staticmethod
    def grade_visualization(fig):
        """Grade a plotly figure based on best practices"""
        score = 0
        feedback = []
        
        if fig.layout.title.text:
            score += 25
            feedback.append("✓ Has title")
        else:
            feedback.append("✗ Missing title")
            
        if fig.layout.xaxis.title.text:
            score += 25
            feedback.append("✓ Has x-axis label")
        else:
            feedback.append("✗ Missing x-axis label")
            
        if fig.layout.yaxis.title.text:
            score += 25
            feedback.append("✓ Has y-axis label")
        else:
            feedback.append("✗ Missing y-axis label")
            
        if len(fig.data) > 0:
            score += 25
            feedback.append("✓ Contains data")
        else:
            feedback.append("✗ No data plotted")
            
        return score, feedback


class QuizGenerator:
    """Generate interactive quizzes"""
    
    def __init__(self):
        self.questions = []
        self.scores = []
        
    def add_question(self, question: str, options: List[str], correct_answer: int):
        """Add a multiple choice question"""
        self.questions.append({
            'question': question,
            'options': options,
            'correct': correct_answer
        })
    
    def create_quiz_widget(self, question_index: int):
        """Create an interactive quiz widget (returns HTML)"""
        q = self.questions[question_index]
        
        html = f"""
        <div style="border: 1px solid #ddd; padding: 15px; border-radius: 5px;">
            <h4>Question {question_index + 1}: {q['question']}</h4>
            <form id="quiz_{question_index}">
        """
        
        for i, option in enumerate(q['options']):
            html += f"""
                <label style="display: block; margin: 10px 0;">
                    <input type="radio" name="q{question_index}" value="{i}">
                    {option}
                </label>
            """
        
        html += """
            </form>
            <button onclick="checkAnswer()" style="margin-top: 10px; padding: 5px 15px;">Submit</button>
            <div id="feedback" style="margin-top: 10px;"></div>
        </div>
        """
        
        return html


def create_environment_checker():
    """Check if all required packages are installed"""
    required_packages = {
        'pandas': 'Data manipulation',
        'numpy': 'Numerical computing',
        'plotly': 'Interactive visualizations',
        'sklearn': 'Machine learning',
        'ipywidgets': 'Interactive widgets'
    }
    
    results = []
    for package, description in required_packages.items():
        try:
            __import__(package)
            results.append(f"✅ {package:<15} - {description}")
        except ImportError:
            results.append(f"❌ {package:<15} - {description} (MISSING)")
    
    return "\n".join(results)


def format_time_remaining(total_minutes: int, elapsed_minutes: int):
    """Format remaining time for session"""
    remaining = total_minutes - elapsed_minutes
    hours = remaining // 60
    minutes = remaining % 60
    
    if hours > 0:
        return f"⏱️ Time remaining: {hours}h {minutes}m"
    else:
        return f"⏱️ Time remaining: {minutes}m"


def create_certificate(student_name: str, completion_date: str, score: int):
    """Generate completion certificate data"""
    certificate = {
        'title': '🏆 Data Science Bootcamp - Introduction Certificate',
        'recipient': student_name,
        'date': completion_date,
        'score': score,
        'skills': [
            'Python Fundamentals',
            'Data Manipulation',
            'Data Visualization',
            'Statistical Analysis',
            'Machine Learning Basics'
        ],
        'instructor': 'Data Science Bootcamp Team'
    }
    return certificate


class MyDataScienceKit:
    """
    🌟 Your Personal Data Science Toolkit
    Enhanced version with professional functionality
    """
    
    def __init__(self, student_name: str = "Data Scientist"):
        self.student_name = student_name
        self.name = f"{student_name}'s Data Science Kit"
        print(f"🚀 {self.name} is ready!")
        print("🎯 Let's build something amazing together!")
        
    def welcome_message(self):
        """A friendly welcome to get you started!"""
        print(f"🌟 Welcome to your Data Science journey, {self.student_name}!")
        print("💡 Remember: Every expert was once a beginner!")
        return "You've got this! 🚀"
    
    def quick_stats(self, data_list):
        """🔍 Tool #1: Quick Stats Explorer (Your First Function!)"""
        if not data_list:
            return "📝 Please provide some data to analyze!"
            
        try:
            stats = {
                '📊 Count': len(data_list),
                '🔢 Average': round(sum(data_list) / len(data_list), 2),
                '⬆️ Highest': max(data_list),
                '⬇️ Lowest': min(data_list),
                '📏 Range': max(data_list) - min(data_list),
                '🎯 Median': sorted(data_list)[len(data_list)//2]
            }
            
            print("🎉 Here are your quick stats:")
            for key, value in stats.items():
                print(f"{key}: {value}")
            
            return stats
        except (TypeError, ValueError) as e:
            return f"❌ Error: Please provide numeric data. {str(e)}"


class PlottingUtils:
    """Professional plotting utilities with bootcamp styling"""
    
    # Bootcamp color palette for engaging visualizations
    COLORS = {
        'primary': '#6C63FF',    # Purple (main brand)
        'secondary': '#FF5E5B',   # Coral (secondary)
        'success': '#00D084',     # Green (success/positive)
        'warning': '#FFB800',     # Gold (attention)
        'danger': '#FF5E5B',      # Coral (alerts)
        'info': '#4ECDC4',        # Teal (information)
        'dark': '#2D3436',        # Dark gray (text)
        'light': '#F8F9FA',       # Light gray (backgrounds)
        'palette': ['#6C63FF', '#00D084', '#FFB800', '#4ECDC4', '#FF5E5B', '#9B59B6', '#3498DB', '#E67E22', '#1ABC9C', '#34495E']
    }
    
    @staticmethod
    def setup_plot_style():
        """Set bootcamp plot styling"""
        plt.style.use('seaborn-v0_8-darkgrid')
        plt.rcParams['figure.figsize'] = (10, 6)
        plt.rcParams['figure.facecolor'] = '#FFFFFF'
        plt.rcParams['font.size'] = 12
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['axes.titlesize'] = 16
        plt.rcParams['axes.labelsize'] = 13
        plt.rcParams['axes.titleweight'] = 'bold'
        plt.rcParams['axes.labelweight'] = 'bold'
        plt.rcParams['xtick.labelsize'] = 11
        plt.rcParams['ytick.labelsize'] = 11
        
    @staticmethod
    def create_bar_chart(data, title="Bar Chart", xlabel="Categories", ylabel="Values", 
                        color_palette=None, figsize=(10, 6)):
        """Create a professional bar chart"""
        PlottingUtils.setup_plot_style()
        
        if color_palette is None:
            color_palette = PlottingUtils.COLORS['palette']
        
        fig, ax = plt.subplots(figsize=figsize)
        
        if isinstance(data, dict):
            x = list(data.keys())
            y = list(data.values())
        else:
            x = range(len(data))
            y = data
            
        bars = ax.bar(x, y, color=color_palette[:len(y)])
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + max(y)*0.01,
                   f'{height}', ha='center', va='bottom', fontweight='bold')
        
        ax.set_title(title, fontweight='bold', pad=20)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.grid(axis='y', alpha=0.3)
        
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        return fig, ax
    
    @staticmethod
    def create_scatter_plot(x, y, title="Scatter Plot", xlabel="X Values", ylabel="Y Values",
                           color=None, size=50, alpha=0.7, figsize=(10, 6)):
        """Create a professional scatter plot"""
        PlottingUtils.setup_plot_style()
        
        fig, ax = plt.subplots(figsize=figsize)
        
        if color is None:
            color = PlottingUtils.COLORS['primary']
            
        scatter = ax.scatter(x, y, c=color, s=size, alpha=alpha, edgecolors='white', linewidth=0.5)
        
        ax.set_title(title, fontweight='bold', pad=20)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        return fig, ax
    
    @staticmethod
    def create_pie_chart(data, title="Pie Chart", figsize=(8, 8), autopct='%1.1f%%'):
        """Create a professional pie chart"""
        PlottingUtils.setup_plot_style()
        
        fig, ax = plt.subplots(figsize=figsize)
        
        if isinstance(data, dict):
            labels = list(data.keys())
            sizes = list(data.values())
        else:
            labels = data.index if hasattr(data, 'index') else range(len(data))
            sizes = data.values if hasattr(data, 'values') else data
        
        colors = PlottingUtils.COLORS['palette'][:len(sizes)]
        
        wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct=autopct, 
                                         startangle=90, colors=colors, 
                                         explode=[0.05] * len(sizes))
        
        # Enhance text appearance
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
            
        ax.set_title(title, fontweight='bold', pad=20)
        plt.tight_layout()
        return fig, ax
    
    @staticmethod
    def create_correlation_heatmap(df, title="Correlation Matrix", figsize=(10, 8)):
        """Create a correlation heatmap with professional styling"""
        PlottingUtils.setup_plot_style()
        
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        corr_matrix = df[numeric_cols].corr()
        
        fig, ax = plt.subplots(figsize=figsize)
        
        im = ax.imshow(corr_matrix, cmap='RdBu_r', aspect='auto', vmin=-1, vmax=1)
        
        # Set ticks and labels
        ax.set_xticks(np.arange(len(corr_matrix.columns)))
        ax.set_yticks(np.arange(len(corr_matrix.columns)))
        ax.set_xticklabels(corr_matrix.columns, rotation=45, ha='right')
        ax.set_yticklabels(corr_matrix.columns)
        
        # Add correlation values
        for i in range(len(corr_matrix.columns)):
            for j in range(len(corr_matrix.columns)):
                text = ax.text(j, i, f'{corr_matrix.iloc[i, j]:.2f}',
                              ha='center', va='center', 
                              color='white' if abs(corr_matrix.iloc[i, j]) > 0.5 else 'black',
                              fontweight='bold')
        
        ax.set_title(title, fontweight='bold', pad=20)
        plt.colorbar(im, ax=ax, label='Correlation Coefficient')
        plt.tight_layout()
        return fig, ax


class DataAnalysisUtils:
    """Utility functions for common data analysis tasks"""
    
    @staticmethod
    def create_data_dictionary(df):
        """Create a data dictionary for a DataFrame"""
        data_dict = []
        for col in df.columns:
            dtype = str(df[col].dtype)
            null_count = df[col].isnull().sum()
            unique_count = df[col].nunique()
            
            if df[col].dtype in ['int64', 'float64']:
                stats = f"Mean: {df[col].mean():.2f}, Std: {df[col].std():.2f}"
            else:
                top_value = df[col].mode().iloc[0] if len(df[col].mode()) > 0 else "N/A"
                stats = f"Top value: {top_value}"
            
            data_dict.append({
                'Column': col,
                'Data Type': dtype,
                'Null Values': null_count,
                'Unique Values': unique_count,
                'Statistics': stats
            })
        
        return pd.DataFrame(data_dict)
    
    @staticmethod
    def detect_outliers(df, column, method='iqr'):
        """Detect outliers in a numeric column"""
        if method == 'iqr':
            Q1 = df[column].quantile(0.25)
            Q3 = df[column].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
        elif method == 'zscore':
            z_scores = np.abs((df[column] - df[column].mean()) / df[column].std())
            outliers = df[z_scores > 3]
        else:
            raise ValueError("Method must be 'iqr' or 'zscore'")
        
        return outliers
    
    @staticmethod
    def analyze_categorical_column(df, column):
        """Comprehensive analysis of a categorical column"""
        analysis = {
            'value_counts': df[column].value_counts(),
            'unique_count': df[column].nunique(),
            'mode': df[column].mode().iloc[0] if len(df[column].mode()) > 0 else None,
            'null_count': df[column].isnull().sum(),
            'null_percentage': (df[column].isnull().sum() / len(df)) * 100
        }
        return analysis


class BootcampEngagement:
    """Enhanced engagement tools for the bootcamp experience"""
    
    @staticmethod
    def create_progress_tracker(current_step, total_steps, section_name=""):
        """Create visual progress tracker for bootcamp sessions"""
        percentage = (current_step / total_steps) * 100
        filled_blocks = int(percentage / 5)  # 20 blocks total
        empty_blocks = 20 - filled_blocks
        
        progress_bar = '█' * filled_blocks + '░' * empty_blocks
        
        print(f"🎯 Progress: [{progress_bar}] {percentage:.1f}%")
        if section_name:
            print(f"📍 Current: {section_name}")
        print(f"✨ Step {current_step} of {total_steps}")
        
        if percentage == 100:
            print("🎉 Congratulations! You've completed this section!")
        
        return percentage
    
    @staticmethod
    def create_celebration(achievement_name, points=10):
        """Create celebration message for achievements"""
        celebration_msg = f"""
🎊 ACHIEVEMENT UNLOCKED! 🎊

✨ {achievement_name} ✨

🏆 You earned {points} points!
💪 Keep up the great work!

{'='*40}
        """
        print(celebration_msg)
        return points
    
    @staticmethod
    def create_engagement_prompt(prompt_text, options=None):
        """Create engaging interactive prompts"""
        print(f"🤔 {prompt_text}")
        if options:
            for i, option in enumerate(options, 1):
                print(f"   {i}. {option}")
        print("Think about your answer... 🧠")
    
    @staticmethod
    def create_insight_box(insight_text, insight_type="discovery"):
        """Create highlighted insight boxes"""
        icons = {
            'discovery': '🔍',
            'key_finding': '🎯', 
            'warning': '⚠️',
            'tip': '💡',
            'celebration': '🎉'
        }
        
        icon = icons.get(insight_type, '💭')
        
        box = f"""
╭─────────────────────────────────────────╮
│ {icon} INSIGHT: {insight_text:<30} │
╰─────────────────────────────────────────╯
        """
        print(box)
    
    @staticmethod
    def create_section_header(section_title, emoji="🚀", description=""):
        """Create engaging section headers"""
        header = f"""

{emoji} {section_title.upper()} {emoji}
{'='*50}
        """
        if description:
            header += f"{description}\n{'='*50}\n"
        
        print(header)
        
    @staticmethod
    def show_next_steps(steps_list):
        """Show clear next steps for students"""
        print("\n🚀 WHAT'S NEXT?")
        print("━" * 30)
        for i, step in enumerate(steps_list, 1):
            print(f"{i}. {step}")
        print("\n💪 You've got this! Keep going!")


class ToolkitShowcase:
    """Showcase data science tools and technologies"""
    
    @staticmethod
    def show_python_ecosystem():
        """Display the Python data science ecosystem"""
        tools = {
            '🐍 Python': 'The programming language that powers it all',
            '📊 Pandas': 'Data manipulation and analysis',
            '🔢 NumPy': 'Numerical computing foundation', 
            '📈 Matplotlib': 'Static, animated, and interactive visualizations',
            '🎨 Seaborn': 'Statistical data visualization',
            '⚡ Plotly': 'Interactive web-based visualizations',
            '🤖 Scikit-learn': 'Machine learning made simple',
            '📓 Jupyter': 'Interactive computing environment',
            '🔗 Git': 'Version control for your projects'
        }
        
        print("🛠️ YOUR DATA SCIENCE TOOLKIT")
        print("═" * 50)
        for tool, description in tools.items():
            print(f"{tool:<15} │ {description}")
        print("═" * 50)
        
    @staticmethod
    def show_career_paths():
        """Display data science career paths"""
        careers = {
            '🕵️ Data Analyst': {
                'description': 'Uncover insights from data to drive business decisions',
                'skills': ['SQL', 'Excel', 'Tableau', 'Statistics'],
                'salary_range': '$60K - $90K'
            },
            '🧪 Data Scientist': {
                'description': 'Build predictive models and advanced analytics',
                'skills': ['Python', 'Machine Learning', 'Statistics', 'Communication'],
                'salary_range': '$90K - $150K'
            },
            '⚙️ ML Engineer': {
                'description': 'Deploy and scale machine learning systems',
                'skills': ['Python', 'Cloud', 'DevOps', 'Deep Learning'],
                'salary_range': '$120K - $180K'
            },
            '🏗️ Data Engineer': {
                'description': 'Build the infrastructure that powers data science',
                'skills': ['SQL', 'Cloud', 'ETL', 'Big Data'],
                'salary_range': '$100K - $160K'
            }
        }
        
        print("🚀 DATA SCIENCE CAREER PATHS")
        print("═" * 60)
        
        for role, info in careers.items():
            print(f"\n{role}")
            print(f"💼 {info['description']}")
            print(f"🎯 Key Skills: {', '.join(info['skills'])}")
            print(f"💰 Salary Range: {info['salary_range']}")
            print("─" * 50)
    
    @staticmethod
    def show_learning_resources():
        """Display curated learning resources"""
        resources = {
            '📚 Essential Books': [
                'Python for Data Analysis by Wes McKinney',
                'Hands-On Machine Learning by Aurélien Géron',
                'The Visual Display of Quantitative Information by Edward Tufte'
            ],
            '🌐 Online Courses': [
                'Kaggle Learn (Free micro-courses)',
                'Coursera Data Science Specialization',
                'edX MIT Introduction to Computer Science'
            ],
            '💬 Communities': [
                'Kaggle Community & Competitions',
                'Reddit r/MachineLearning',
                'Data Science Discord Servers'
            ],
            '🛠️ Practice Platforms': [
                'Kaggle Datasets & Competitions',
                'Google Colab for free computing',
                'GitHub for portfolio building'
            ]
        }
        
        print("📖 RECOMMENDED LEARNING RESOURCES")
        print("═" * 50)
        
        for category, items in resources.items():
            print(f"\n{category}")
            for item in items:
                print(f"  • {item}")
        print("\n🎯 Remember: The best way to learn is by doing!")