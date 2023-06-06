from prefect_email import EmailServerCredentials

def create_email_credentials():
    credentials = EmailServerCredentials(
        username="EMAIL_PLACEHOLDER",
        password="APP_PASSWORD_PLACEHOLDER",  # must be an app password
    )
    credentials.save("nys-gmail")

if __name__ == "__main__":
    create_email_credentials()