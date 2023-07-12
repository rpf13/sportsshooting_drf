# SportsShooting - DRF API

The "SportsShooting DRF API" is a site, which acts as the API for the related React Front End project `INSERT LINK HERE`. It will provide the necessary backend and API functionality, to be consumed by the React frontend application.

---

## User Stories

---

## Wireframes

The Wireframes are the prototype of this project and show the base idea and the skeleton of the app. Even though this repo is mainly used for the API backend, the Wireframes of the frontend application do still have a crucial impact, since they define the data to be consumed.. I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

<details>
<summary>Mobile Wireframe</summary>


</details>

<details>
  
<summary>Desktop Wireframe</summary>
  
![Main Site](docs/wireframes/desktop/d_main.png)
![Sign Up](docs/wireframes/desktop/d_match_detail.png)
![Login](docs/wireframes/desktop/d_myschedule.png)
![Logout](docs/wireframes/desktop/d_shooters.png)
![Dashboards](docs/wireframes/desktop/myguns.png)
![Contact](docs/wireframes/desktop/d_profile.png)

</details>

---

## Data Model

The following ERD (Entity Relationship Diagram) displays the SQL database schema and the associated models, used to create this project. It shows the underlaying fundament of the individual models and their relation to it.

![ERD](docs/images/sportsshooting_erd.png)

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
