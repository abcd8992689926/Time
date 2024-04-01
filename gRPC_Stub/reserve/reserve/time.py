from datetime import datetime
import json

from repositories.future import Future

if __name__ == '__main__':
    with open('config/connection.json') as f:
        config = json.load(f)
    db_url = config['connectionString']
    print(db_url)
    modelFuture = Future(
        db_url=db_url,
        user_id='test',
        title='testTitle',
        content='testContent',
        Datetime=datetime.utcnow()
    )
    modelFuture.add(modelFuture)
