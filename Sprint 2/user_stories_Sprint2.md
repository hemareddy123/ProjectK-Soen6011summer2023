| Epic                                                         | User Story                                                              | Acceptance Criteria                                                                                      | Story-Points | Risk Description                     | Impact    |  Probability | Counter measure           | 
|--------------------------------------------------------------|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|--------------|---------------------------------------|-----------|--------------|---------------------------|
| As a user, I want to securely log in to the career service platform | As a user, I should be able to create an account in case I already do not have one. | Users should be prompted to create a new account if the email ID entered is not registered in the system database. | 2            | There’s a risk that user might encounter issues while creating a new account | Medium | Low | Testing of Login module and providing a feedback mechanism for the users facing this problem
|                                                               | As a user having an account, I want to securely log in using my user ID and password. | Users should be able to securely log in to the career service platform using user ID and password and access platform services. Users entering incorrect credentials should fail the login process and should be displayed a failed login message. | 2 | There is a risk that the login functionality may have security vulnerabilities, potentially exposing user accounts to unauthorized access or attacks| High | Medium to High | Using a secure authorization method, hashing the password, introducing rate limit on account login attempts to prevent brute force attacks|                                                            
| As an employer, I want to add/manage a job postings and shortlist candidates,resumes on the career services platform |As an employer I want to view a dashboard upon login | Employers should be able to view and use the dashboard and dashboard elements |2 | There is a risk that the dashboard might fail to render information| Low to medium | Low to medium |Make sure that the application has strong connection with the database and retrieves information correctly|
|                                                                                                                      |As an employer I want to Add job, specifying its details and then finally posting it in the platform| The employer should be able to add all the required details of a job and the job should be saved onto the database and should be available to be viewed online | 3 | There is a risk that job might not be saved into the database |Low  |Low | It is important to commit all the necessary changes into the database before an operation is closed |
|                                                              |As an employer I want to view list of job seekers/students| The list of students open to work should be available to recruiters/employers who are hiring |3 | NA |NA | Na |Na |
|   |As an employer, I want to select students for interviews who have applied for a particular job| The list of students who applied for a job should be separately visible to the employer |3| There is a risk that wrong set of students might have applied for the job | High| Low |It is important to provide the employer with a user interface which will enable him/her to clearly describe job requirements, so as to eliminate any ambiguity.|
|   |As an employer, I want to view all the jobs that I have posted| A list of jobs created and posted by the user employer should be available to the user itself, clearly available from the dashboard| 2 |There is a risk that the information of posted job might not be consistent with the information retrieved| High | Low | If the employer is not able to view all the posted job, it reduces user experience. Its important to maintain database information consistency across the platform |













