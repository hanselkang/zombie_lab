from db.run_sql import run_sql
from models.human import Human
from models.zombie import Zombie
from models.biting import Biting

def save(biting):
    sql = "INSERT INTO bitings (human_id, zombie_id) VALUES (%s, %s) RETURNING id"
    values = [biting.human.id, biting.zombie.id]
    results = run_sql(sql, values)
    biting.id = results[0]['id']
    return biting

def select_all():
    bitings = []
    sql = "SELECT * FROM bitings"
    results = run_sql(sql)
    for row in results:
        biting = Biting(row['id'],row['zombie_id'],row['human_id'])
        bitings.append(biting)
    return bitings


def delete_all():
    sql = "DELETE FROM bitings"
    run_sql(sql)

def select(id):
    biting = None
    sql = "SELECT * FROM bitings WHERE id = %s"
    values = [id]
    results = run_sql(sql,values)
    if len(results) > 0:
        result = results[0]
        biting = Biting(result['human_id'],result['zombie_id'],result['id'])
    
    return biting