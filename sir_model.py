import numpy as np


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


def deriv_susceptible_wrt_time(beta, susceptible, infectious, total_population):
    '''
    assume that susceptible will always decrease given
    the nature of this disease transm e.g. assumed immunity
    '''
    return -beta * susceptible * (infectious / total_population)


def derivatives_helper(initial_conditions, time_grid, total_population, beta, mean_recov_rate):
    '''
    facilitates the odeint solver from scipy

    notes: time_grid param is not explicitly use
           initial recov'd value is not explicitly used
           from initial_conditions
    '''
    susceptible, infectious, _ = initial_conditions

    dSdt = deriv_susceptible_wrt_time(beta, susceptible, infectious, total_population)



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


    # each derivative is a funct of time, so we set up a numpy array for time that we'll use in calc's and plotting
    time_grid = np.linspace(0, days, days)

    # Set initial conditions for our diffEQ solver
    initial_conditions = (initial_susceptible, initial_infected, initial_recovered)

    # TODO: use ode solver to integrate the SIR equations



    ### DISPLAY FIELDS ###
    print(f', total_population:{total_population}\n, days: {days}\n, initial_infected: {initial_infected}\n, initial_recovered: {initial_recovered}\n, recovery_period_in_days: {recovery_period_in_days}\n, avg_num_contacts_per_person: {avg_num_contacts_per_person}\n, proba_of_disease_transm: {proba_of_disease_transm}\n, initial_susceptible: {initial_susceptible}\n, beta: {beta}\n, mean_recov_rate: {mean_recov_rate}\n, time_grid: {time_grid.shape}')