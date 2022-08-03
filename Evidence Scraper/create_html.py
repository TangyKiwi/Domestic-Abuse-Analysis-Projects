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
        f.write(create_item(df["text"].iloc[i], df["surrounding_text"].iloc[i], df["link"].iloc[i]))
        i += 1

    f.close()


def create_label(date):
    label = '<!-- timeline time label -->\n' + \
            '<div class="time-label">\n' + \
            '  <span class="bg-blue">' + date + '</span>\n' + \
            '</div>\n' + \
            '<!-- /.timeline-label -->\n'
    return label


def create_item(header, body, footer):
    item = '<!-- timeline item -->\n' + \
           '<div>\n' + \
           '  <i class="fas fa-arrow-alt-circle-right bg-blue"></i>\n' + \
           '  <div class="timeline-item">\n' + \
           '    <h3 class="timeline-header"><a href="#">' + str(header) + '</a></h3>\n' + \
           '    <div class="timeline-body">' + str(body) + '</div>\n' + \
           '    <div class="timeline-footer">\n' + \
           '      <a class="btn btn-primary btn-sm" href="' + str(footer) + '" target="_blank">Link</a>\n' + \
           '    </div>\n' + \
           '  </div>\n' + \
           '</div>\n' + \
           '<!-- END timeline item -->\n'
    return item


create_html("Data/Depp_Heard/Depp/timexy_depp_times.csv", "timeline_depp.html")
create_html("Data/Depp_Heard/Heard/timexy_heard_times.csv", "timeline_heard.html")