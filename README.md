
# Output Difference Script  
  
## Description  
  
This Python script is designed to compare two input files, each containing lexicographically sorted ASCII strings, and will produce two output files:  
  
- The 1st output file will contain strings found only in the 1st input file and not in the 2nd.  
- The 2nd output file will contain strings found only in the 2nd input file and not in the 1st.  
  
The results are saved in two separate files within an "Output" directory.  
  
## Requirements  
  
- Python 3.x  
  
## Usage  
  
1. Run the script using the following command:  

    python3 main.py  

2. You will be prompted to provide the paths for two input files:  
  

    Please enter the path for input file 1: [Your path for the first file]  
    Please enter the path for input file 2: [Your path for the second file]  
  
3. After processing, the script will save unique strings from each file in two separate output files within the "Output" directory.  
  
## Notes
  
- It's essential to ensure that the input files are lexicographically sorted.  
- The two input paths should point to different files. The script will raise an error if the same file is provided for both inputs.  
  
## Troubleshooting  
  
If you encounter the error "permission denied", ensure that the Python script has the necessary permissions to access the specified files or directories. If the error persists, please check the provided file paths for accuracy.