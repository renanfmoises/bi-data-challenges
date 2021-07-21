### Background & objectives

Your work to help *HandyHelp* to better seize the market continues. Now you are interested into looking at the types of complaints made in NYC.

### Specs

**IMPORTANT**: You have to **deliver the URL of your script with all your SQL queries.** Same thing than in *HandyHelp Big Query analysis I.* Make sure that the script is running without errors before delivering.

---

Again, as we are planning for the 2021 workforce allocation, **filter** in all your queries calls/complaints **from 2020**. Answer the following questions: 

1. What are New Yorkers complaining the most about (*complaint type*)? Order the complaints in descending order. 
2. You think that this first query might be interesting for other analysis and it will be used by other data team members. Store it as a view (using the Editor commands not the *Save as*... ) in a dataset called `handyhelp`
    <details><summary markdown='span'>Hint 💡
    </summary>
      When you add your SQL code to create the view in your script don't write the name of the project preceding the handyhelp dataset. e.g: instead of `myfirstproject-xxxx.handyhelp.complaints_view` use `handyhelp.complaints_view`(only dataset.table).
    </details>

3. There are several noise related issues in NYC (Noise-Residential, Noise - Street/Sidewalk…) To appreciate the real scale of it, aggregate all the noise related issues and compare it with the rest of complaints (in %). 
4. What is the average resolution time of problems?
    Need help?

    <details><summary markdown='span'>Help ❔
    </summary>
      To obtain the resolution time you could create a column that subtract 'closed_date' to 'opened_date'. Also in the WHERE clause filter out all resolution times = 0.
    </details>



5. What is the average resolution time of each complaint type? 
6. What is the borough where the complaints are solved faster?
7. You want to asses what complaints take more time to resolve. With that information you can better allocate the offer to the demand per borough. What are the slowest complaints (=longest resolution time) to be solved in each borough? 
- Note

    Filter out boroughs with null  values and Unspecified

7. You want to assess whether to include a pest control professional/fumigator category in the platform. Is there a real demand for that in NYC? To decide about it you analyze how often (times per day) a rodent is reported in NYC.

### Key learning points

- Keep practicing your SQL knowledge to solve analytical questions
- Create Views
- Use date/timestamp/time functions in your queries
