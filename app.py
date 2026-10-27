import streamlit as st

# 1. Display the project title
st.title("Insurance Premium Estimator")
st.write("Calculate an estimated annual health insurance premium.")
st.info("This calculator uses sample rates for an academic project.")

# 2. Collect the customer's age
age = st.number_input(
    "Enter your age",
    min_value=18,
    max_value=100,
    value=25
)

# 3. Select an insurance plan
plan = st.selectbox(
    "Select your insurance plan",
    ["Basic", "Standard", "Premium"]
)

# 4. Select a coverage amount
coverage = st.selectbox(
    "Select coverage amount",
    [300000, 500000, 1000000],
    format_func=lambda x: f"₹{x:,}"
)

# 5. Number of family members covered
family_members = st.number_input(
    "Number of family members covered",
    min_value=1,
    max_value=10,
    value=1
)

# 6. Optional critical illness coverage
critical_illness = st.checkbox(
    "Add critical illness coverage"
)

# 7. Sample base premiums
plans = {
    "Basic": 3000,
    "Standard": 5000,
    "Premium": 8000
}

# 8. Calculate the age adjustment
if age < 30:
    age_charge = 0
elif age <= 45:
    age_charge = 1000
else:
    age_charge = 2000

# 9. Calculate the coverage adjustment
if coverage == 300000:
    coverage_charge = 0
elif coverage == 500000:
    coverage_charge = 1000
else:
    coverage_charge = 2000

# 10. Calculate the family coverage charge
family_charge = (family_members - 1) * 1000

# 11. Calculate the critical illness charge
if critical_illness:
    critical_charge = 1500
else:
    critical_charge = 0

# 12. Retrieve the base premium
base_premium = plans[plan]

# 13. Calculate the total annual premium
total_premium = (
    base_premium
    + age_charge
    + coverage_charge
    + family_charge
    + critical_charge
)

# 14. Display the premium breakdown
st.subheader("Your Premium Breakdown")

st.write(f"Base premium: ₹{base_premium:,.2f}")
st.write(f"Age adjustment: ₹{age_charge:,.2f}")
st.write(f"Coverage adjustment: ₹{coverage_charge:,.2f}")
st.write(f"Family coverage adjustment: ₹{family_charge:,.2f}")
st.write(f"Critical illness charge: ₹{critical_charge:,.2f}")

# 15. Display the final estimated premium
st.success(
    f"Estimated Annual Premium: ₹{total_premium:,.2f}"
)

# 16. Display a disclaimer
st.caption(
    "For academic demonstration only. "
    "These sample rates are not actual insurance quotes."
)