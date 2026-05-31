# DataPipe

## Description:
    DataPipe is a learning project to practice different methods and tools of software development, data analysis and software optimisation.
    ### Goals:
        1) Build fully functional and reusable ML project.
        2) Get comfortable with using git daily.
        3) Practice writing pytests.
        4) Writing AI agents with and without special frameworks.
        5) Learn rust as a tool to make optimisations.
    ### How does it work:
        For now it has only one dataset "car_sales_analysis_dataset.csv"(I plan to make it a universal tool for diferent kind of datasets in future, but I have to start somewhere so...).
        This project uses  generator functions to handle large datasets in future. For now it can read the csv file and filter it by conditions wich user can choose, then write it to new csv file.
        
## How to use:
    call datapipe --input name_of_inputed_csv_file.csv --filter name_of_needed_filter --output name_of_output_file.csv
    to see filter options - datapipe --help
    --output argument is fully optional it has a default name for result file
    
