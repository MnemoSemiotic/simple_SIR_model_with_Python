
### FUNCTIONS LIVE UP HERE ###
def get_initial_susceptible(total_population, initial_infected, initial_recovered):
    '''
    Everyone not initially_infected is naively
    considered susceptible initially
    '''
    return total_population - initial_infected - initial_recovered



if __name__ == "__main__":
    ### THESE ARE OUR PARAMETERS ###

    # Assume a "closed" population (related to S)
    total_population = 100000

    # Number of days in consideration
    days = 200

    initial_infected = 100
    initial_recovered = 0

    # parameter to build avg recovery rate (gamma)
    recovery_period_in_days = 10

    # params to build beta, our transmission rate from susceptible to infectious
    avg_num_contacts_per_person = 5 # per day
    proba_of_disease_transm = 0.04 # of acquiring the disease AND encountering a person with the disease




    ### THIS IS OUR PROCEDURE ###
    # simply the total population minus the initial infected and initial recovered
    initial_susceptible = get_initial_susceptible(total_population, initial_infected, initial_recovered)