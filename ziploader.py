import os
import time
import zipfile
import random
import string

def generate_random_word(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def create_data_file(file_name, words_count):
    with open(file_name, 'w') as f:
        words = [generate_random_word(random.randint(3, 100)) for _ in range(words_count)]
        f.write('\n'.join(words))

def generate_unique_name(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def main():
    data_counter = 0
    
    # Get user input for the directory path
    zip_folder_path = input("Enter the directory path where you want to save the generated data: ")
    words_count = 1000000  # Number of words per data file
    
    try:
        os.makedirs(zip_folder_path, exist_ok=True)
        zipf = zipfile.ZipFile(os.path.join(zip_folder_path, 'data_files.zip'), 'a')
        
        temp_files_to_delete = []  # Keep track of temporary files
        
        while True:
            unique_name = generate_unique_name(10)
            data_file_name = os.path.join(zip_folder_path, f"{unique_name}.txt")
            
            while os.path.exists(data_file_name):
                unique_name = generate_unique_name(10)
                data_file_name = os.path.join(zip_folder_path, f"{unique_name}.txt")
            
            create_data_file(data_file_name, words_count)
            zipf.write(data_file_name, os.path.basename(data_file_name))
            
            # Add the file to the list of temporary files to delete
            temp_files_to_delete.append(data_file_name)
            
            data_counter += 1
            
            print(f"File {data_counter} generated.")

    except KeyboardInterrupt:
        print("\nUser interrupted. Stopping data generation.")
    finally:
        zipf.close()
        
        # Delete the temporary files
        for temp_file in temp_files_to_delete:
            os.remove(temp_file)
            
        print("Temporary files deleted.")
        print("Data generation completed.")  # Display completion message

if __name__ == "__main__":
    main()
