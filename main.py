from json import loads

from flask import Flask

app = Flask(__name__)

with open('candidates.json', encoding='utf-8') as file:
    data = loads(file.read())


@app.route('/')
def main_page() -> str:
    """
    Вывод список все кандидатов
    """
    new_list = []
    for candidate in data:
        a = (f'<pre>'
             f'Имя кандидата - {candidate["name"]}'
             f'\nПозиция кандидата - {candidate["position"]}'
             f'\nНавык кандидата {"".join(candidate["skills"])}'
             f'</pre>')
        new_list.append(a)
    return ' '.join(new_list)


@app.route('/candidate/<candidate_id>')
def get_candidate(candidate_id: str) -> str:
    """
    Выводит кандидата по его уникальному ID
    """
    if candidate_id.isdigit() is False or int(candidate_id) > len(data):
        return f'У нас нет информации о кандидате с ID {candidate_id}'
    for candidate in data:
        if candidate['id'] == int(candidate_id):
            return (f'<img src="{candidate["picture"]}">'
                    f'<pre>'
                    f'Имя кандидата - {candidate["name"]}'
                    f'\nПозиция кандидата - {candidate["position"]}'
                    f'\nНавык кандидата {"".join(candidate["skills"])}'
                    f'</pre>')


@app.route('/skill/<prof_skill>')
def get_skill_of_candidate(prof_skill: str) -> str:
    """
    Выводи список кандидатов, у которых имеется переданный prof_skill
    """
    new_list = []
    for candidate in data:
        if prof_skill.lower() in "".join(candidate["skills"]).lower().split(", "):
            a = (f'<pre>'
                 f'Имя кандидата - {candidate["name"]}'
                 f'\nПозиция кандидата - {candidate["position"]}'
                 f'\nНавык кандидата {"".join(candidate["skills"])}'
                 f'</pre>')
            new_list.append(a)

    return ' '.join(new_list)


if __name__ == "__main__":
    app.run()
