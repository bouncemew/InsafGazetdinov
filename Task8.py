def render_input(func):
    def render_output(field):
        res = func(field)
        a = f'"<p>"{res}"</p>"'
        return a, print(a)

    return render_output


@render_input
def render(field):
    return f'<input id="id_{field}" name="{field}">'


render('username')
