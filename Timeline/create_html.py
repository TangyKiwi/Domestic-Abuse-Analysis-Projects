import pandas as pd
from pathlib import Path


def create_html(input_dir, output_dir):
    df = pd.read_csv(input_dir)
    filepath = Path(output_dir)
    filepath.parent.mkdir(parents=True, exist_ok=True)

    f = open(output_dir, "w")
    i = 0
    cur_month = ""
    for date in df["pretty_date"]:
        date = str(date)
        if cur_month != date:
            f.write(create_label(date))
            cur_month = date
        #f.write(create_item(df["text"].iloc[i], df["surrounding_text"].iloc[i], df["link"].iloc[i]))
        f.write(create_item(df["text"].iloc[i], df["name"].iloc[i], df["surrounding_text"].iloc[i], df["link"].iloc[i]))
        i += 1

    f.close()


def create_label(date):
    label = '<!-- timeline time label -->\n' + \
            '<div class="time-label">\n' + \
            '  <span class="bg-blue">' + date + '</span>\n' + \
            '</div>\n' + \
            '<!-- /.timeline-label -->\n'
    return label


def create_item(span, header, body, footer):
    item = '<!-- timeline item -->\n' + \
           '<div>\n' + \
           '  <i class="fas fa-arrow-alt-circle-right bg-blue"></i>\n' + \
           '  <div class="timeline-item">\n' + \
           '    <span class="time">' + str(span) + '</span>\n' + \
           '    <h3 class="timeline-header"><a href="#">' + str(header) + '</a></h3>\n' + \
           '    <div class="timeline-body">' + str(body) + '</div>\n' + \
           '    <div class="timeline-footer">\n' + \
           '      <a class="btn btn-primary btn-sm" href="' + str(footer) + '" target="_blank">Link</a>\n' + \
           '    </div>\n' + \
           '  </div>\n' + \
           '</div>\n' + \
           '<!-- END timeline item -->\n'
    return item


# create_html("Data/timexy_depp_v_ngn_closing_annex.csv", "HTML Outputs/timeline_annex.html")
# create_html("Data/timexy_depp_v_ngn_closing_claimant.csv", "HTML Outputs/timeline_claimant.html")
# create_html("Data/timexy_depp_v_ngn_closing_defendant.csv", "HTML Outputs/timeline_defendant.html")
create_html("Data/Depp/timexy_depp_times.csv", "HTML Outputs/depp_witness_statements.html")
create_html("Data/Heard/timexy_heard_times.csv", "HTML Outputs/heard_witness_statements.html")