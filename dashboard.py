import streamlit as st

st.set_page_config(
    page_title="Stack Overflow Salary Analysis",
    layout="wide"
)

# ======================================================
# EXECUTIVE SUMMARY
# ======================================================

st.title("2025 Stack Overflow Developer Survey Dashboard")

st.header("Executive Summary")

st.success("""
Remote workers earn significantly more than hybrid workers.

The average salary difference is approximately $16,900.

Bachelor's degree holders earn significantly less than Master's and Professional degree holders.

No statistically significant salary difference was found between Master's and Professional degree holders.
""")

# ======================================================
# QUESTION 1
# ======================================================

st.markdown("---")
st.header("Question 1: Exploratory Data Analysis")

st.subheader("Average Job Satisfaction by Job Title")

st.image("figure1_jobsatisfaction.png")

st.write("""
Retired respondents reported the highest average job satisfaction. Several senior technical roles also reported above-average satisfaction levels.
""")

st.subheader("Mean Salary by Job Title")

st.image("figure2_salaryjob.png")

st.write("""
Engineering managers, software architects, and DevOps professionals reported the highest average salaries.
""")

st.subheader("Annual Salary vs Age")

st.image("figure3_salaryage.png")

st.write("""
Salary varies significantly across age groups, suggesting additional factors influence compensation.
""")

# ======================================================
# QUESTION 2
# ======================================================

st.markdown("---")
st.header("Question 2: Hybrid vs Remote Work")

st.subheader("Descriptive Statistics")

st.table({
    "Statistic":["Sample Size",
                 "Mean Salary",
                 "Median Salary"],
    "Hybrid":["7803",
              "$101,790",
              "$77,730"],
    "Remote":["6934",
              "$118,684",
              "$90,528"]
})

st.subheader("Two-Sample t-Test")

st.write("""
t-statistic = -2.5907

p-value = 0.0096

Conclusion: Remote workers earn significantly more than hybrid workers.
""")

st.subheader("Bootstrap Results")

st.image("q2_bootstrap_means.png")

st.image("q2_difference_means.png")

st.image("q2_standardized.png")

st.subheader("Confidence Intervals")

st.table({
    "Method":[
        "Formula-Based",
        "Bootstrap"
    ],
    "95% CI":[
        "(-29,675, -4,112)",
        "(-30,910, -4,755)"
    ]
})

st.subheader("Median Salary Comparison")

st.table({
    "Method":[
        "Mood's Median Test",
        "Bootstrap Median Test"
    ],
    "p-value":[
        "1.40E-25",
        "0.5805"
    ]
})

# ======================================================
# QUESTION 3
# ======================================================

st.markdown("---")
st.header("Question 3: Education Level Analysis")

st.subheader("Mean Salaries")

st.table({
    "Education":[
        "Bachelor's",
        "Master's",
        "Professional"
    ],
    "Mean Salary":[
        "$160,988",
        "$182,220",
        "$197,701"
    ]
})

st.subheader("ANOVA Results")

st.table({
    "Statistic":[
        "F-statistic",
        "p-value"
    ],
    "Value":[
        "17.4966",
        "2.70 x 10^-8"
    ]
})

st.write("""
At least one education group differs significantly in mean salary.
""")

st.subheader("Bootstrap Analysis")

st.image("q3_bootstrap_means.png")

st.image("q3_pairwise_means.png")

st.image("q3_standardized.png")

st.subheader("Pairwise Confidence Intervals")

st.table({
    "Comparison":[
        "Bachelor - Master",
        "Bachelor - Professional",
        "Master - Professional"
    ],
    "95% CI":[
        "(-32653, -11529)",
        "(-60985, -16293)",
        "(-41283, 7488)"
    ]
})

st.write("""
Bachelor's degree holders earned significantly less than both Master's and Professional degree holders.
No significant difference was found between Master's and Professional degree holders.
""")