from app import create_app

# EB looks for an 'application' callable by default.
application = create_app()

if __name__ == "__main__":
    application.run()
