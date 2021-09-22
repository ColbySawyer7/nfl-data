YEARS = range(1999, 2022)[::-1]
COLLAPSE_WIDGET = '''
    <details {{#open}}open{{/open}}>
        <summary>{{title}}</summary>
        {{#contents}}
            {{& pywebio_output_parse}}
        {{/contents}}
    </details>
    '''