
### FUNCTIONS LIVE UP HERE ###
def get_initial_susceptible(total_population, initial_infected, initial_recovered):
    '''
    Everyone not initially_infected is naively
    considered susceptible initially
    '''
    return total_population - initial_infected - initial_recovered

def get_beta(avg_num_contacts_per_person, proba_of_disease_transm):
    '''
    beta is the avg number of contacts per person,
    per day, multiplied by the proba of disease transm
    in a contact between a susceptible preson and 
    an infectious person
    susceptible --> infectious
    '''
    return avg_num_contacts_per_person * proba_of_disease_transm


def get_mean_recov_rate(recovery_period_in_days):
    '''
    mean recovery/mortality rate (gamma), 1 over how many
    days it takes a person to recover
    '''
    return 1.0 / recovery_period_in_days


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


    # transm rate from susceptible to infectious
    beta = get_beta(avg_num_contacts_per_person, proba_of_disease_transm)


    # gamma, mean transmission rate from infectious to recovered
    mean_recov_rate = get_mean_recov_rate(recovery_period_in_days)







    ### DISPLAY FIELDS ###
    print(f'total_population:{total_population}\n, days: {days}\n, initial_infected: {initial_infected}\n, initial_recovered: {initial_recovered}\n, recovery_period_in_days: {recovery_period_in_days}\n, avg_num_contacts_per_person: {avg_num_contacts_per_person}\n, avg_num_contacts_per_person: {avg_num_contacts_per_person}\n, proba_of_disease_transm: {proba_of_disease_transm}\n, initial_susceptible: {initial_susceptible}\n, beta: {beta}\n')