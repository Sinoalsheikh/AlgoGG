# CI/CD Configuration for Web Application
class CICDConfig:
    def __init__(self):
        self.configurations = {
            "build_command": "npm run build",
            "test_command": "npm test",
            "deploy_command": "aws s3 sync build/ s3://lvlhub-web/",
            "environment": "production"
        }

    def display_configurations(self):
        for key, value in self.configurations.items():
            print(f"{key}: {value}")

# Example usage
if __name__ == "__main__":
    cicd_config = CICDConfig()
    cicd_config.display_configurations()
