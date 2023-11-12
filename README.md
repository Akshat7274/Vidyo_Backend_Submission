# Vidyo_Backend_Submission

### Run the API using Docker
To run the docker image which hosts the backend code, run the following command
```
docker run -d -p 8000:8000 zeleus/vidyo-backend
```

### Set up on Local Environment
1. Download the source code and open terminal in the root folder of the project
2. Set up a virtual environment:
```
python -m venv venv
```
3. Activate the virtual environment:
```
.\venv\Scripts\activate //For Windows
source venv/bin/activate //For Linux and MAC
```
4. Install the dependencies:
```
pip install -r requirements.txt
```
5. Setup the Database:
```
python manage.py makemigrations
```
6. Complete migrations:
```
python manage.py migrate
```
7. Create admin user:
```
python manage.py createsuperuser
```
8. Run the server:
```
python manage.py runserver
```
