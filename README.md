# SportsShooting - DRF API

The "SportsShooting DRF API" is a site, which acts as the API for the related React Front End project [SportsShooting](https://github.com/rpf13/sportsshooting_react). It will provide the necessary backend and API functionality, to be consumed by the React frontend application.

Link to deployed DRF API site: [SportsShooting DRF API](https://sportsshooting-drf-rpf13-5060e23f8756.herokuapp.com/)

Link to deployed React Frontend site: [SportsShooting Deployed](https://sportsshooting-rpf13-d2b23798b278.herokuapp.com/)

Link to Frontend React GitHub repo: [SportsShooting Repo](https://github.com/rpf13/sportsshooting_react)

---

## User Stories

### Setup and Documentation
- As a Developer I can create the README of the project so an interested user can verify my work and follow up the development process
- As a Developer I can create the TESTING part of the documentation so an interested user can verify the testing process
- As a Developer I can create the initial DRF setup and link all necessary tools and libraries so that I can start developing the project.

### Profiles

- As a Developer I can create a new user, which will automatically create a profile for this user, so I can use the features only available for registered users
- As a Developer I can list all created profiles, so I can use this information for further processing
- As a Developer I can edit my profile, so I can add further information to my profile
- As a Developer I can delete my profile and all it's linked content, so my account will be completely erased from the API - STRETCH OBJECTIVE

### Matches

- As a Developer I can create a new match so that it is visible in the matches list
- As a Developer I can view the match details so that I can see additional information
- As a Developer I can view a list of all matches so that I can use it for further processing
- As a Developer I can edit a match created by me so that I can update or correct it
- As a Developer I can delete a match created by me so it will no longer be available via the API
- As a Developer I can create count attending and count comments object including a filter option so that I can use this cumulated data in my frontend app and use the filter for it
- As a Developer I can create a search feature so I can search based on match, location, date or shooter
- As a Developer I can create a pre defined category filter so I can use it to create a type filter for level type of match

### Comment

- As a Developer I can create a comment so it will be available via the API to be used and linked to a match
- As a Developer I edit a comment created by me so I can update its data
- As a Developer I can delete a comment created by me so it will no longer be availabe via the API
- As a Developer I can list all comments so I can use it for further processing and filtering
-As a Developer I can add a filter feature to the comments app** so that I can see all comments added to a particular match

### MySchedule / Attending - content visible to particular user

- As a Developer I can create an attending object for a match I am going so I can use it for further processing via the API
- As a Developer I can delete an attending object, which I have created so I can access / update the API with this information
- As a Developer I can view all attending objects I have created so I can use it for further processing via the API
- As a Developer I can create a filter feature so that I can filter matches based on a particular user, so I can see for each user, which matches he will attend.

### MyGuns - content visible to particular user

- As a Developer I can create a new gun item so that it is visible in the MyGuns list
- As a Developer I can update a gun item so that I can correct or change its data
- As a Developer I can delete a gun item so that it will no longer exist via the API
- As a Developer I can create a pre defined category filter so I can use it to create a type filter for handgun or rifle

### Shooters / Messages - STRETCH OBJECTIVE

- As a Developer I can view / list all profiles created so I can use partial information to be seen via the API in my frontend application
- As a Developer I can create a search feature so that I can search based on the shooters name or club
- As a Developer I can create a message to another shooter so I can see the created message via the API
- As a Developer I can update a message I have created so I can update its data via the API
- As a Developer I can delete a message I have created so it will no longer be available via the API
- As a Developer I can view a message sent to me, so I can see read the content and reply to it

### Final Deployment and React Readines

- As a Developer I can deploy the app to Heroku and ElephantSQL so I can access the final production app to use it in my React Frontend application
- As a Developer I can add the necessary steps required to link the React FrontEnd application to the backend so I can start developing the React app
- As a Developer I can add JWT functionality to my REST api so that I can do "base" JWT authentication with my React app
- As a Developer I can refactor the existing JWT solution with tokens in local storage to a JWT httpOnly cookie solution** so that **my application gets more secure and JS has no longer access to the local storage tokens

---

## Data Model

The following ERD (Entity Relationship Diagram) displays the SQL database schema and the associated models, used to create this project. It shows the underlaying fundament of the individual models and their relation to it.

![ERD](docs/images/sportsshooting_erd.png)

---

## Features


---

## Tools & Technologies Used


---

## Development

The following chapters describe why and how I have choosen to code certain parts the way they are. This section should give an explanation to my thinking process and explain the reader some conceptual decisions.

### Commit messages

I have decided to mostly use multiline commit messages. Commit messages are an essential part of the whole project and a single line commit message is just not enough to explain. After reading [this interesting article](https://cbea.ms/git-commit/), it was clear to me, that I have to use it.

I have decided to use (mostly) multiline commits, but using tags as described this [cheatsheet](https://cheatography.com/albelop/cheat-sheets/conventional-commits/) or as also described in the LMS of the Code Institute. I did use the following syntax guidline:
- **feat:** for feature which may or may not include a CSS part
- **fix:** for a bugfix
- **style:** for changes to CSS or to give style to the code itself
- **docs:** for changes related to documentation
- **refactor:** for refactored code, re-written code
- **maint:** for general maintenance

---

## Agile Development Process

### Github Projects
[Github Projects](https://github.com/users/rpf13/projects/6/views/1) has been used as the Agile tool during the development phase of this project. The Kanban board was very useful to keep track on the tasks. I have created 4 columns (ToDo, In Progress, On Hold, Done) and moved the stories accordingly. 
The On Hold column has served as a "parking spaces", when a story was partially done, but not completely finished.

![Github Projects Kanban Board](docs/images/github_projects.png)

### GitHub Issues
[Github Issues](https://github.com/rpf13/sportsshooting_drf/issues) has been used to create all the stories, before they were placed on the projects Kanban board. I have created an issues templates to simplify creation.
Each issue has a label for the MoSCoW prioritization.

Once a story has been created via the template, it will be automatically added to the Kanban board in the Todo column.

![Github Issues](docs/images/github_issues.png)

### MoSCoW Prioritization

The MoSCoW prioritization has been used to divide all epics and stories into the following categories:

- MustHave: guaranteed to be delivered
- ShouldHave: adds significant value, but not mandatory for MVP
- CouldHave: adds value, would be nice to have
- WontHave: no priority for this iteration, acts as placeholder for future implementation

A related Github label has been created for each category and added to each epic, story - which makes it easy to identify and see the value it brings.

---

## Testing

Testing is covered in a separate page, view [TESTING.md](TESTING.md)

---

## Deployment


---

## Credits

### Code

### Content

### Media


---

### Acknowledgements

