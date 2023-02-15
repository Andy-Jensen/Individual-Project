# Individual-Project: Predictions on Minor Conflicts and Wars

# Project Description:
Life is the most precious thing on the planet. Parents raise children who then become parents themselves. We don't always know which lives will be cut short, but we can try to reduce it. Wars and minor armed conflicts take many lives and in this project I will be predicting, based on the data, the time from the start date of a conflict to the date a minimum of 25 lives are lost. With better knowledge of preperation time, hopefully more lives can be saved!

# Project Goals:
* Run an end to end data science project
* Build a model that will accurately predict the time until a minimum of 25 lives are lost (time_to_conflict)
* Explore and discover drivers of time_to_conflict
* Accumulate and deliver all information in a final report

# Initial Hypothesis:
My first thoughts after looking at the dataset made me think that region and type_of_conflict were going to be the most significant drivers.

# Project Plan:

* Acquire the data from "https://ucdp.uu.se/downloads/index.html#armedconflict"
  * "UCDP/PRIO Armed Conflict Dataset version 22.1"

* Data prep for exploration:
    * Unnecessary columns were dropped
        * total columns were reduced from 28 to 12 (11 original columns and 1 engineered column)
    * Target variable was engineered from the `start_date` and `start_date2` columns
        * This returned a value (in days) for how long from the beginning of the conflict it took for the conflict to accumulate at least 25 casualties
    * Nulls were valuable:
        * Nulls were in `side_a_2nd`, `side_b_2nd`, and `territory_name`
            * `side_a_2nd` and `side_b_2nd` were encoded to a `0` or `1` depending if they had an ally or not
            * `territory_name` nulls were changed to "government" since null values were indicating there was no territorial conflict and that it was a govermental conflict
    * There were an initial 2568 rows
        * The total number of rows was reduced to 294 because there were entries for each "episode" of the war (often on a yearly basis) and I just use the initial entry to predict the `time_to_conflict`

* Separate into train, validate, and test datasets
 
* Explore the train data in search of drivers of time_to_conflict
   * Answer the following initial questions
       * Is the average time to conflict for countries in Asia significantlly higher compared to all other regions?
       * Is the average time to conflict for countries in Africa and the Middle East significantlly lower than the average time to conflict for all regions?
       * Is the average time to conflict for countries that have an intrastate conflict over government significantlly greater than the average time to conflict for countries that have an interstate conflict over territory?
       * Is the average time to conflict for countries that have an internationalized intrastate conflict significantly less than the average time to conflict for all conflicts in the dataset?
       
* Prep the data for modeling:
    * encode columns to reduce the number of catagories:
        * `location` intiger 0-10 for top ten locations and other
        * `side_a` intiger 0-10 for top ten side_a's and other
        * `side_b` intiger 0-20 for top twenty side_b's and other
        * `start_date` intiger 0 or 1, 0 if before 2000 and 1 if after 2000
        * `time_to_conflict` 1= less than or equal to 30 days, 2= between 30 days and 1 year, 3= longer than a year
    * Dummies were encoded for:
        * `location`, `side_a`, `side_b`, `start_date`, `type_of_conflict`, `region`, `time_to_conflict`, and `incompatibility`
    * Dropped columns:
        * `territory_name` and `start_date2`
      
* Develop a model to predict the `time_to_conflict`
   * Use drivers identified in explore to build predictive models
       * Decision Tree
       * KNN
       * Random Forest
       * Linear Regression
   * Evaluate models on train and validate data
   * Select the best model based on highest accuracy and difference between in sample and out of sample data
   * Test the best model on test data
 
* Draw conclusions

# Data Dictionary:

* The description of the data can be found in the Data Codebook located here:
    * https://ucdp.uu.se/downloads/ucdpprio/ucdp-prio-acd-221.pdf


| Feature | Definition |
|:--------|:-----------|
|conflict_id| The unique identifier of the conflict|
|location| The name of the country/countries whose String government(s) has a primary claim to the incompatibility. Note that this is not necessarily the geographical location of the conflict.|
|side_a| The name of the country/countries of Side A in a conflict. Always the government side in intrastate conflicts. Note that this is a primary party to the conflict.|
|side_a_id| The unique identifier of the actor on side A. Note that in contrast with older versions of UCDP datasets, this variable is NO LONGER the Gleditsch and Ward state identifier (GWcode or GWNo). Use the gwno_a variable instead.|
|side_a_2nd| side_a_2nd lists all states that enter a conflict with troops to actively support side A. By definition, only independent states can be a secondary party in conflict. A secondary warring party on side A shares the position in the incompatibility with Side A in the conflict. side_a_2nd does not need to meet the 25 battle-related deaths criterion to be included in the dataset; an active troop participation is enough. Comma separated if multiple.|
|side_b| Identifying the opposition actor or country/countries of side B in the conflict. In an intrastate conflict, this includes a military opposition organization. Note that this is a primary party to the conflict. Comma separated if multiple.|
|side_b_id| The identifier of each of the actors on side B in the conflict. Note that in contrast with older versions of UCDP datasets, this variable is NO LONGER the Gleditsch and Ward state identifier (GWcode or GWNo) if the conflict is interstate and Side B represents a country. Use the gwno_b variable instead. If more than one opposition organization or state is involved in a conflict, this is a comma-separated list of values.|
|side_b_2nd| side_b_2nd lists all states that enter a conflict with troops to actively support side B. By definition, only independent states can be a secondary party in conflict. A secondary warring party on side B shares the position in the incompatibility with Side B in the conflict. Side_b_2nd does not need to meet the 25 battle-related deaths criterion to be included in the dataset; an active troop participation is enough. Note that when there is more than one opposition organization listed in an intrastate conflict, the dataset does not provide information on which of these groups the state coded as Side B Secondary is supporting. Comma separated if multiple.|
|incompatibility| The main conflict issue identified per the UCDP definitions: 1= Incompatibility about territory 2= Incompatibility about government 3= Incompatibility about government AND territory|
|territory_name| The name of the territory over which the conflict is fought, provided that the incompatibility is over territory. In case the two sides use different names for the disputed territory, the name listed is the one used by the opposition organisation. One reason for this is that this is most often the name that the general public recognises. Another reason is that there are cases where the disputed territories do not have an official name.|
|year| The year of observation (1946-2021).|
|intensity_level| The intensity level in the conflict per calendar year. The intensity variable is coded in two categories: 1= Minor: between 25 and 999 battle-related deaths in a given year. 2= War: at least 1,000 battle-related deaths in a given year.|
|cumulative_intensity| This variable takes into account the temporal dimension of the conflict. It is a dummy variable that codes whether the conflict since the onset has exceeded 1,000 battle-related deaths. For conflicts with a history prior to 1946, it does not take into account the fatalities incurred in preceding years. A conflict is coded as 0 as long as it has not over time resulted in more than 1,000 battle-related deaths. Once a conflict reaches this threshold, it is coded as 1.|
|type_of_conflict| One of the following four types of conflict: 1 = extrasystemic (between a state and a non-state group outside its own territory, where the government side is fighting to retain control of a territory outside the state system) 2 = interstate (both sides are states in the Gleditsch and Ward membership system). 3 = intrastate (side A is always a government; side B is always one or more rebel groups; there is no involvement of foreign governments with troops, i.e. there is no side_a_2nd or side_b_2nd coded) 4 = internationalized intrastate (side A is always a government; side B is always one or more rebel groups; there is involvement of foreign governments with troops, i.e. there is at least ONE side_a_2nd or side_b_2nd coded)|
|start_date| The date, as precise as possible, of the first battle-related death in the conflict. The date is set after the conflict fulfils all criteria required in the definition of an armed conflict, except for the number of deaths.|
|start_prec| The level of precision for the initial start date.|
|start_date2| The date, as precise as possible, when a given episode of conflict activity reached 25 battle-related deaths in a year. Thus, for each episode of a conflict, a new Startdate2 is coded. In case precise information is lacking, Startdate2 is by default set to 31 December. An episode is defined as continuous conflict activity. Consequently, a new episode is coded whenever a conflict restarts after one or more year(s) of inactivity.|
|start_prec2| The level of precision for start_date2.|
|ep_end| A dummy variable that codes whether the conflict is inactive the following year and an episode of the conflict thus ends. If the conflict is inactive the following year(s), this variable is coded as 1. If not, a 0 is coded. For the latest year in the dataset, it is unknown whether the conflict will be recorded as active or inactive in the following year, and the variable is always given the code 0.|
|ep_end_date| This variable is only coded in years where ep_end has the value 1. If a conflict year is followed by at least one year of conflict inactivity, the ep_end_date variable lists, as precise as possible, the date when conflict activity ended.|
|ep_end_prec| The level of precision for episode end.|
|gwno_a| The Gleditsch and Ward country codes of side_a. Comma separated if multiple.|
|gwno_a_2nd| The Gleditsch and Ward country codes of side_a_2nd. Comma separated if multiple.|
|gwno_b| The Gleditsch and Ward country codes of side_b. Comma separated if multiple.|
|gwno_b_2nd| The Gleditsch and Ward country codes of side_b. Comma separated if multiple.|
|gwno_loc| The Gleditsch and Ward country codes of the incompatibility. Comma separated if multiple.|
|region| The region of the incompatibility: 1 = Europe (GWNo: 200-399) 2= Middle East (GWNo: 630-699) 3= Asia (GWNo: 700-999) 4= Africa (GWNo: 400-626) 5= Americas (GWNo: 2-199).|
|version| The version of the dataset: 22.1|
|time_to_conflict| The difference in days between `start_date` and `start_date2`.|

# Steps to Reproduce
1. Clone this repo
2. Use the function from prepare to prepare and obtain the data from the website
3. Run the explore and modeling notebook
4. Run final report notebook
