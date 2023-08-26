def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    num_males = int (input("Enter number of male students: "))
    num_females = int (input("Enter number of female students: "))
    totalstudents = num_males + num_females
    print("Number of male students: ", num_males)
    print("Number of female students: ", num_females)
    print("Number of total students: ", totalstudents)
    m_perc = (num_males/totalstudents)*100
    print("Percent of male students: ", (format(m_perc, '.2f')))
    f_perc = (num_females/totalstudents)*100
    print("Percent of female students: ", (format(f_perc, '.2f')))
    
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
