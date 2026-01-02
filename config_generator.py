import os
import json

def generate_config():
    production_env = os.environ.get("PRODUCTION", "false").lower() == "true"
    api_port = os.environ.get("API_PORT", 5000)
    
    if production_env:
        config_data = {"DDBB-SERVER": "PRODUCTION", "API-PORT": api_port}
    else:
        config_data = {"DDBB-SERVER": "DEVELOPMENT", "API-PORT": api_port}
        
    with open("config.json", "w") as config_file:
        json.dump(config_data, config_file, indent=4)
    print(f"El puerto es {api_port}")    
    print(f"la compilación:  {production_env}")   
if __name__ == "__main__":
    print("Generating configuration file...")
    generate_config()
