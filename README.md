# HRI Privacy

### Setup
```
sudo apt update
sudo apt install postgresql postgresql-contrib
pip install -e .
pip install -r requirements.txt
sudo nano /etc/postgresql/12/main/postgresql.conf        # Change listen addresses to *
```

### Development
Add rules, constraints, and assumptions to `src/rules.py`.
Add conversation samples to `data` and `data/metadata`. Copy and paste the existing conversation examples `data/conversation1/` and `data/metadata/conversation1.py`.
Edit `src/test.py` constants to specific content_id and person_id pairs or uncomment `test_loop()` to loop through all content_id and person_id pairs