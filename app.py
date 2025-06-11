import streamlit as st

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital Resume | Narasimha Naidu Nagam"
PAGE_ICON = ":waving_hand:"
NAME = "Narasimha Naidu Nagam"
DESCRIPTION = "Machine Learning Trainee | Versatile professional with 4+ years of experience in the Oil & Gas industry, now transitioning to Machine Learning with hands-on experience in developing and deploying predictive models using various algorithms. Proficient in evaluating model accuracy and selecting optimal solutions. Experienced in deploying machine learning applications using Flask, Streamlit, Docker Desktop, and Kubernetes. Eager to leverage acquired skills and contribute to future machine learning endeavors with a highly motivated and results-oriented approach."
EMAIL = "nagamnaidu3@gmail.com"
PHONE = "+91 9492252452, +91 9515874452"
LINKEDIN = "https://www.linkedin.com/in/nagam-narasimha-naidu-836a92176/"
GITHUB = "https://github.com/NagamNaidu"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- CSS FOR WHITE BACKGROUND AND ANIMATIONS ---
st.markdown(
    """
    <style>
    body {
        color: #000;
        background-color: #fff;
    }
    .stApp {
        background-color: #fff;
    }
    .fade-in {
        animation: fadeIn ease 1s;
        -webkit-animation: fadeIn ease 1s;
        animation_fill_mode: forwards;
    }
    @keyframes fadeIn {
        0% {opacity:0;}
        100% {opacity:1;}
    }
    @-webkit-keyframes fadeIn {
        0% {opacity:0;}
        100% {opacity:1;}
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- HEADER SECTION ---
with st.container():
    st.header("New Portfolio")
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write("Email:", EMAIL)
    st.write("Phone:", PHONE)
    cols = st.columns(2)
    with cols[0]:
        st.markdown(f"""
            <a href="{LINKEDIN}" target="_blank">
                <img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" width="30" height="30">
                LinkedIn
            </a>
            """, unsafe_allow_html=True)
    with cols[1]:
        st.markdown(f"""
            <a href="{GITHUB}" target="_blank">
                <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="30" height="30">
                GitHub
            </a>
            """, unsafe_allow_html=True)

# --- TABS ---
objective, experience, education, skills, projects = st.tabs(["Career Objective", "Experience", "Education", "Skills", "Projects"])

# --- OBJECTIVE TAB ---
with objective:
    st.header("Career Objective")
    st.write(
        """
        Highly motivated and quick-learning individual seeking a machine learning trainee position to leverage foundational knowledge and contribute to innovative projects. 
        Eager to develop practical skills in data analysis, model building, and algorithm implementation within a collaborative environment. 
        Passionate about applying machine learning techniques to solve real-world problems and contribute to advancements in the field.
        """
    )
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)

# --- EXPERIENCE TAB ---
with experience:
    st.header("Experience")
    st.subheader("Software Engineer (Trainee) – Lyros Technology Pvt. Ltd | Jan 2025 – Present")
    st.write(
        """
        - Assisted in collecting, cleaning, and structuring datasets for AI/ML training and analysis.
        - Ensured data integrity and optimized data processing workflows.
        - Supported in designing, training, and evaluating machine learning models.
        - Conducted model performance testing and suggested improvements for better accuracy and efficiency.
        - Analyzed AI applications and proposed optimization strategies.
        - Improved computational efficiency and enhanced model scalability.
        - Stayed updated with the latest AI/ML advancements and contributed to research initiatives.
        - Documented findings and assisted in integrating new AI methodologies into existing projects.
        - Wrote basic scripts to automate repetitive tasks and improve AI development workflows.
        - Assisted in integrating AI solutions with DevOps automation where applicable.
        - Maintained clear and concise documentation of AI/ML experiments, model performance, and project progress.
        - Shared insights and findings with the team for continuous improvement.
        - Worked closely with data scientists, software engineers, and DevOps teams to support AI/ML projects.
        - Actively participated in brainstorming sessions and provided innovative solutions.
        """
    )
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)

# --- EDUCATION TAB ---
with education:
    st.header("Education")
    st.subheader("B.Tech in Petroleum Technology Engineering")
    st.write("Aditya Engineering College (2015 – 2019) | Percentage: 75%")
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)

# --- SKILLS TAB ---
with skills:
    st.header("Skills")
    st.write("- Web Development: HTML, CSS, JavaScript, ReactJS, Tailwind CSS, Bootstrap CSS, Streamlit")
    st.write("- Programming Languages: JavaScript, Python")
    st.write("- AI/ML Tools: NumPy, Pandas, Matplotlib, Scikit-learn, Jupyter Notebook")
    st.write("- Version Control: Git, GitHub")
    st.write("- IDE/Tools: Visual Studio Code, Redux Toolkit, Jupyter Notebook")
    st.write("- Knowledge of deep learning frameworks such as Tensor Flow or PyTorch.")
    st.write("- Familiarity with data visualization tools (e.g., Matplotlib, Seaborn) and cloud-based ML platforms.")
    st.write("- Exposure to version control systems (e.g., Git).")
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)

# --- PROJECTS TAB ---
with projects:
    st.header("Projects")
    st.subheader("Swiggy Clone")
    st.write(
        """
        - Developed a responsive Swiggy-like food delivery application using ReactJS and Tailwind CSS.
        - Applied Atomic Design principles, Redux Toolkit, and React Hooks for state management.
        - Built features including dynamic restaurant listings, cart system, and mobile-optimized UI.
        """
    )
    st.subheader("Patient Datasets Project: Disease Prediction")
    st.write(
        """
        * Objective: Develop a predictive model for disease diagnosis or prognosis using patient datasets.
        * Data Processing & Feature Engineering: Implement robust data cleaning, transformation, and feature engineering techniques to prepare patient data for modeling. Explore methods for handling missing values, outliers, and imbalanced datasets.
        * Model Selection & Optimization: Evaluate and compare various machine learning models (e.g., logistic regression, support vector machines, decision trees, neural networks) for disease prediction. Employ techniques like cross-validation, hyperparameter tuning, and ensemble methods to optimize model performance.
        * Performance Metrics & Evaluation: Rigorously evaluate model performance using appropriate metrics such as accuracy, precision, recall, F1-score, AUC-ROC, and calibration curves. Analyze and interpret model results to identify key predictors and potential biases.
        * Reporting & Visualization: Create clear and concise reports summarizing the project methodology, results, and conclusions. Utilize visualizations (e.g., feature importance plots, ROC curves, confusion matrices) to effectively communicate findings.
        """
    )
    st.subheader("Machine Learning Project: Image Recognition")
    st.write(
        """
        * Objective: Develop a classification model for image recognition tasks.
        * Data Preprocessing & Augmentation: Implement image preprocessing techniques such as resizing, normalization, and data augmentation to improve model robustness and generalization.
        * Model Architecture & Training: Design and train a convolutional neural network (CNN) architecture for image classification. Explore different CNN architectures (e.g., ResNet, Inception, EfficientNet) and transfer learning techniques.
        * Model Optimization & Regularization: Employ techniques like dropout, batch normalization, and weight decay to prevent overfitting and improve model generalization. Optimize model hyperparameters using techniques like grid search or Bayesian optimization.
        * Performance Evaluation & Analysis: Evaluate model performance using metrics such as accuracy, precision, recall, and F1-score. Analyze misclassified images to identify potential areas for improvement.
        * Visualization & Interpretation: Visualize model activations and feature maps to gain insights into how the model is learning and making predictions. Use techniques like Grad-CAM to highlight important regions in the input images.
        * Correlation Heatmaps: Generate and interpret correlation heatmaps to understand the relationships between different features or model parameters.
        """
    )

# --- FOOTER SECTION ---
st.markdown("""---""")
st.write(":copyright: 2025 | Narasimha Naidu Nagam")

# --- STREAMLIT CLOUD DEPLOYMENT ---
st.sidebar.header("Streamlit Cloud Deployment")
st.sidebar.write("1. Create a GitHub repository for your portfolio.")
st.sidebar.write("2. Sign up for a Streamlit Cloud account.")
st.sidebar.write("3. Connect your GitHub repository to Streamlit Cloud.")
st.sidebar.write("4. Deploy your app!")

    
st.sidebar.markdown("[My Portfolio](https://share.streamlit.io/yourusername/yourrepository)")  # Replace with your actual Streamlit Cloud link