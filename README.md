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
 
* Explore the train data in search of drivers of churn
   * Answer the following initial questions
       * Does higher monthly charges cause churn?
       * Does wether customers have dependents cause them to churn more or less?
       * Does having DSL cause customers to churn more or less?
       * Are customers with a lower tenure more or less likely to churn?
       * Is internet service causing churn?
       * Is no online security causing churn?
      
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
|side_a_2nd| side_a_2nd lists all states that enter a conflict with troops to actively support side A. By definition, only independent states can be a secondary party in conflict. A secondary warring party on side A shares the position in the incompatibility with Side A in the conflict.
side_a_2nd does not need to meet the 25 battle-related deaths criterion to be included in the dataset; an active troop participation is enough. Comma separated if multiple.|
|side_b| Identifying the opposition actor or country/countries of side B in the conflict. In an intrastate conflict, this includes a military opposition organization. Note that this is a primary party to the conflict. Comma separated if multiple.|
|side_b_id| The identifier of each of the actors on side B in the
conflict. Note that in contrast with older versions of UCDP datasets, this variable is NO LONGER the Gleditsch and Ward state identifier (GWcode or GWNo) if the conflict is interstate and Side B represents a country. Use the gwno_b variable instead. If more than one opposition organization or state is involved in a conflict, this is a comma-separated list of values.|
|side_b_2nd| side_b_2nd lists all states that enter a conflict with troops to actively support side B. By definition, only independent states can be a secondary party in conflict. A secondary warring party on side B shares the position in the incompatibility with Side B in the conflict. Side_b_2nd does not need to meet the 25 battle-related deaths criterion to be included in the dataset; an active troop participation is enough. Note that when there is more than one opposition organization listed in an intrastate conflict, the dataset does not provide information on which of these groups the state coded as Side B Secondary is supporting. Comma separated if multiple.|
|incompatibility| The main conflict issue identified per the UCDP definitions:
1= Incompatibility about territory
2= Incompatibility about government
3= Incompatibility about government AND territory|
|device_protection| Yes or No, wether the customer has device_protection or not|
|tech_support| Yes or No, wether the customer has tech_support or not|
|streaming_tv| Yes or No, wether the customer has tv streaming or not|
|streaming_movies| Yes or No, wether the customer has movie streaming or not|
|paperless_billing| Yes or No, wether the customer has enrolled in paperless billing or not|
|monthly_charges| how much each customer pays per month|
|total_charges| how much each customer has payed in their tenure|
|churn| Yes or No, wether the customer has left the company or not|
|contract_type| current contract length of each customer|
|internet_service_type| the type of internet each customer is paying for|
|payment_type| how each customer is sending their payment to Telco|
|signup_date| date of each customers enrollment with Telco|
|churn_month| month that the customer left Telco. 'None' if the customer is still enrolled|

# Steps to Reproduce
1. Clone this repo
2. Use the function from acquire and prepare to obtain the data from the Codeup SQL server using the programmed query
3. Run the explore and modeling notebook
4. Run final report notebook
