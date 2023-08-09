
## User Acceptance Tests

## User Story: As a user, I should be able to create an account in case I already do not have one so that I can use the platform and apply for jobs.

**Test Steps:**
1. Go to the website login page
2. Click on the register/ signup button
3. Fill in the required information
4. Click on Create an account / sign up button

**Expected Result:**
- The user should receive a notification about successful account creation

**Actual Result:**
- The user was able to create an account and get notified about it successfully

## User Story: As a user having an account, I want to securely log in using my user ID and password so that I can view my dashboard and avail all the functionalities provided by the platform.

**Test Steps:**
1. Go to the website login page
2. Fill in the email-id and password
3. Click on log-in or sign in

**Expect Result:**
- The user should be taken to the profile creation page (on his/her/their) first sign-in, or the dashboard upon subsequent sign-ins.

**Actual Result:**
- The user was taken to the profile creation page and then the user dashboard.

## User Story: As an employer, I want to view a dashboard upon login, so that I can view the jobs and access functionalities with ease

**Test Steps:**
1. Go to the website login page
2. Sign in using employer credentials

**Expect Result:**
- The employer should be introduced to his/her/their dashboard where they can access functionalities from the left side of the dashboard menu and see their posted jobs upfront in the dashboard

**Actual Result:**
- The employer was successfully taken to the dashboard.

## User Story: As an employer I want to Add job, specifying its details and then finally posting it on the platform so that students can view and apply for jobs as per their requirements

**Test Steps:**
1. Log in using the appropriate employer credential
2. Click on ‘add a job’/ ‘post a job’ button from the left panel of the dashboard
3. On the new page, add job information in the given form
4. Click on the ‘post’ or ‘submit’ button

**Expect Result:**
- The employer should be notified about successfully posting the job. If a mandatory field is missing, the job should not be posted and the user should be shown an error message accordingly about the missing field

**Actual Result:**
- The employer was able to (1) successfully post a job upon adding all required information in the field. (2) was shown an error in case of missing fields in the form

## User Story: As an employer, I want to view the list of job seekers/students so that I can assess candidates.

**Test Steps:**
1. From the dashboard, click on ‘applied candidates’

**Expect Result:**
- The employer should be able to see all applied candidates on the next page in a tabular format

**Actual Result:**
- The employer was able to successfully view all the applied candidates.

## User Story: As an employer, I want to select students for interviews who have applied for a particular job so that I can shortlist promising candidates and assess them in interviews

**Test Steps:**
1. From the dashboard, click on the ‘applied candidates’ button to view all the candidates who applied for posted jobs
2. On the next page, scroll horizontally to the right to view the ‘Select for interview’ button.
3. Click on the button to select the appropriate candidates

**Expect Result:**
- The employer should be able to select candidates, and the selected candidates should be moved to the ‘shortlisted candidate’ section

**Actual Result:**
- The employer was able to select candidates for an interview and put them in the shortlist candidate section

## User Story: As an employer, I want to view all the jobs that I have posted so that I can keep track of job postings and manage them efficiently.

**Test Steps:**
1. After adding jobs successfully, go back to the dashboard homepage
2. The posted jobs should be visible directly on the dashboard homepage
3. If there is no job posted, this would be empty

**Expect Result:**
- The employer should be able to see all posted jobs directly on the dashboard homepage

**Actual Result:**
- The employer was able to view all posted jobs successfully on the dashboard homepage directly.

## User Story: As a student, I want to securely log on to the career service platform, create a profile, and upload a resume so that recruiters can view my profile and get appropriate information about me.

**Test Steps:**
1. Go to the website login page
2. Use your user credential to fill out the form
3. Click on the ‘sign-in’ button
4. A new user will be introduced to a create a-profile page
5. Fill in that form and upload your resume through upload a file button
6. Click on the submit button to finalize the process of profile creation.

**Expect Result:**
- The student user would get a profile creation page as a form and can view his/her profile after creating it from the dashboard

**Actual Result:**
- The student user is successfully able to create a profile for themselves and access it from the dashboard

## User Story: As a student, I should be able to use a dashboard once I log in so that I can use all the features available on it

**Test Steps:**
1. Go to the website login page
2. Use the correct user credential to fill in the email-id and password
3. Click on the sign-in button

**Expect Result:**
- A successful login should take the user to a new webpage which would display the student dashboard, with all the functionalities listed on the left side of the dashboard in a menu

**Actual Result:**
- The student user is successfully shown a dashboard with all required functionalities available on the left side of the dashboard in a menu

## User Story: As a student, I should be able to search for jobs so that I can view and assess my options

**Test Steps:**
1. Go to the website login page
2. Use the correct user credential to fill in the email-id and password
3. Click on the sign-in button
4. View the dashboard

**Expect Result:**
- A successful login should take the user to a new webpage which would display the student dashboard, which would present all the latest job cards posted by recruiters

**Actual Result:**
- The student user is successfully shown a dashboard with all job posting cards directly accessible from the dashboard

## User Story: As a student, I should be able to apply for jobs so that I can fulfil my need of applying to multiple jobs

**Test Steps:**
1. Log on to the website using student credentials
2. View the multiple job cards posted by recruiters
3. Click on a job of your liking
4. Select the apply button on the card

**Expect Result:**
- A successful apply operation would let the student know that they have successfully applied for that job through a notification

**Actual Result:**
- The student gets notified about the successful application for the job once they click on the apply button through a notification

## User Story: As a student, I should be able to view the jobs I have applied for so that I can assess my options and finalize my choice

**Test Steps:**
1. Log on to the website using student credentials
2. In the dashboard, on the left side, click on the ‘applied jobs’ button

**Expect Result:**
- This should take the user to a page where they can view all the jobs they have applied for in a tabular format

**Actual Result

:**
- The student gets to see all the jobs they have applied for in a list.

## User Story: As an employer, I want to see, manage and update the status of received job applications so that I can make sure my posted job reflects the latest changes

**Test Steps:**
1. Logon to the website using user credentials
2. In the dashboard, view the cards of job posted by the employer
3. Click on the ‘update’ button on the required card of job posting

**Expect Result:**
- This should take the user to the edit page of job posting, and they can edit details as per their needs

**Actual Result:**
- The employer user is successfully able to update the job listings as per their needs

## User Story: As an admin, I want to view all user's profiles' information (employer/ candidate) so that I can manage them.

**Test Steps:**
1. Go to the login page of the website
2. Login as admin using proper credentials
3. In the dashboard, click on ‘view all users’

**Expect Result:**
- This would take the admin user to a new page where they can view all the users

**Actual Result:**
- The admin is successfully able to view all the users (employers and students) in a list/ tabular form.

## User Story: As an admin, I want to delete any student or employer profile so that I can remove unauthorized or malicious users

**Test Steps:**
1. Go to the login page of the website
2. Login as admin using proper credentials
3. In the dashboard, click on ‘view all users’
4. Scroll horizontally to see the ‘delete’ button for each user
5. Click on the delete button

**Expect Result:**
- This would result in the deletion of that particular account, and it's erased from the database too

**Actual Result:**
- The admin is successfully able to delete users
