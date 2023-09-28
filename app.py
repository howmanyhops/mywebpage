from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Obtiene los valores del formulario
    hours_worked = float(request.form['hours_worked'])
    hours_knocking = float(request.form['hours_knocking'])
    doors = float(request.form['doors'])
    eligible_interactions = float(request.form['eligible_interactions'])
    hops = float(request.form['hops'])
    ref_properties = float(request.form['ref_properties'])
    sign_ups = float(request.form['sign_ups'])

    # Realiza los cálculos (igual que en tu código Python original)
    interaction_rate = (eligible_interactions / doors) * 100
    absolute_hop_rate = (hops / doors) * 100
    absolute_sign_up_rate = ((hops + ref_properties + sign_ups) / doors) * 100
    sign_up_per_hour = (hops + ref_properties + sign_ups) / hours_knocking
    good_ref = (hops * 2) + ref_properties
    sign_up_rate = (hops + ref_properties + sign_ups) / eligible_interactions

    # Retorna los resultados como respuesta HTML
    return render_template('calculator.html',
                           interaction_rate=interaction_rate,
                           absolute_hop_rate=absolute_hop_rate,
                           absolute_sign_up_rate=absolute_sign_up_rate,
                           sign_up_per_hour=sign_up_per_hour,
                           good_ref=good_ref,
                           sign_up_rate=sign_up_rate)

if __name__ == '__main__':
    app.run(debug=True)
