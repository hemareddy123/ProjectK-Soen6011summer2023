# User Acceptance Tests

## User story: Create an Account
**Test Steps:**
1. Go to the website login page.
2. Click on the register/signup button.
3. Fill in the required information.
4. Click on the "Create an account" / "Sign up" button.

**Expected Result:** The user should receive a notification about successful account creation.

**Actual Result:** The user was able to create an account and received a successful notification.

## User story: Secure Log In
**Test Steps:**
1. Go to the website login page.
2. Fill in the email ID and password.
3. Click on "Log in" or "Sign in".

**Expected Result:** The user should be taken to the profile creation page on their first sign-in, or the dashboard upon subsequent sign-ins.

**Actual Result:** The user was taken to the profile creation page and then to the user dashboard.

## User story: View Dashboard as Employer
**Test Steps:**
1. Go to the website login page.
2. Sign in using employer credentials.

**Expected Result:** The employer should see their dashboard with access to functionalities and posted jobs.

**Actual Result:** The employer was successfully taken to the dashboard.

## User story: Add and Post a Job
**Test Steps:**
1. Log in using appropriate employer credentials.
2. Click on "Add a Job" / "Post a Job" button in the dashboard.
3. Fill in job information in the provided form.
4. Click on the "Post" or "Submit" button.

**Expected Result:** The employer should be notified about successfully posting the job. If mandatory fields are missing, an error message should appear.

**Actual Result:** The employer was able to successfully post a job with all required information and received error messages for missing fields.

## User story: View List of Job Seekers/Students
**Test Steps:**
1. From the dashboard, click on "Applied Candidates".

**Expected Result:** The employer should see all applied candidates in a tabular format on the next page.

**Actual Result:** The employer was able to view all applied candidates successfully.

## User story: Select Students for Interviews
**Test Steps:**
1. From the dashboard, click on the "Applied Candidates" button.
2. Scroll horizontally to the right to find the "Select for Interview" button.
3. Click on the button to select appropriate candidates.

**Expected Result:** The employer should be able to select candidates, and the selected candidates should be moved to the "Shortlisted Candidates" section.

**Actual Result:** The employer was able to select candidates for interviews and move them to the shortlist candidate section.

## User story: View Posted Jobs
**Test Steps:**
1. After adding jobs successfully, return to the dashboard homepage.

**Expected Result:** The employer should be able to see all posted jobs directly on the dashboard homepage. If no jobs are posted, the section should be empty.

**Actual Result:** The employer was able to view all posted jobs successfully on the dashboard homepage.

