def lap_details(**kwargs):
    print("===My Laptop Details===")
    for key,value in kwargs.items():
        print(f"{key} :{value}")
# lap_details(Company="HP",Model="Victus 15",RAM="8GB",GPU="RTX 2050")


Company = input("Enter the Company Name:")
Model = input("Enter the model:")
RAM = input("RAM size(ex.8gb,16gb):")
GPU = input("GPU series: ")
lap_details(Company=Company,Model=Model,RAM=RAM,GPU=GPU)