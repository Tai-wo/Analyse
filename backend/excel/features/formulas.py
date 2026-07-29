import openpyxl


class ExcelFormulaEngine:

    def __init__(self, workbook_path):

        self.workbook_path = workbook_path

        self.workbook = openpyxl.load_workbook(workbook_path)

        self.sheet = self.workbook.active

        self.report = []

    # -----------------------------
    # Basic Formulas
    # -----------------------------

    def sum(self, output_cell, start_cell, end_cell):

        self.sheet[output_cell] = f"=SUM({start_cell}:{end_cell})"

        self.report.append(f"SUM -> {output_cell}")

    def average(self, output_cell, start_cell, end_cell):

        self.sheet[output_cell] = f"=AVERAGE({start_cell}:{end_cell})"

        self.report.append(f"AVERAGE -> {output_cell}")

    def minimum(self, output_cell, start_cell, end_cell):

        self.sheet[output_cell] = f"=MIN({start_cell}:{end_cell})"

        self.report.append(f"MIN -> {output_cell}")

    def maximum(self, output_cell, start_cell, end_cell):

        self.sheet[output_cell] = f"=MAX({start_cell}:{end_cell})"

        self.report.append(f"MAX -> {output_cell}")

    def count(self, output_cell, start_cell, end_cell):

        self.sheet[output_cell] = f"=COUNT({start_cell}:{end_cell})"

        self.report.append(f"COUNT -> {output_cell}")

    # -----------------------------
    # Conditional
    # -----------------------------

    def if_formula(self, output_cell, condition, true_value, false_value):

        self.sheet[output_cell] = f'=IF({condition},"{true_value}","{false_value}")'

        self.report.append(f"IF -> {output_cell}")

    def ifs_formula(self, output_cell, *conditions):

        formula = "=IFS("

        formula += ",".join(conditions)

        formula += ")"

        self.sheet[output_cell] = formula

        self.report.append(f"IFS -> {output_cell}")

    # -----------------------------
    # Lookup
    # -----------------------------

    def vlookup(self, output_cell, lookup_value, table_range, column, exact=True):

        exact_value = "FALSE" if exact else "TRUE"

        self.sheet[output_cell] = (

            f'=VLOOKUP({lookup_value},{table_range},{column},{exact_value})'

        )

        self.report.append(f"VLOOKUP -> {output_cell}")

    def xlookup(self,

                output_cell,

                lookup_value,

                lookup_array,

                return_array):

        self.sheet[output_cell] = (

            f'=XLOOKUP({lookup_value},{lookup_array},{return_array})'

        )

        self.report.append(f"XLOOKUP -> {output_cell}")

    def index_match(self,

                    output_cell,

                    return_range,

                    lookup_value,

                    lookup_range):

        formula = (

            f'=INDEX({return_range},MATCH({lookup_value},{lookup_range},0))'

        )

        self.sheet[output_cell] = formula

        self.report.append(f"INDEX MATCH -> {output_cell}")

    # -----------------------------
    # COUNTIFS
    # -----------------------------

    def countif(self,

                output_cell,

                range_cells,

                criteria):

        self.sheet[output_cell] = (

            f'=COUNTIF({range_cells},"{criteria}")'

        )

        self.report.append(f"COUNTIF -> {output_cell}")

    def sumif(self,

              output_cell,

              range_cells,

              criteria,

              sum_range):

        self.sheet[output_cell] = (

            f'=SUMIF({range_cells},"{criteria}",{sum_range})'

        )

        self.report.append(f"SUMIF -> {output_cell}")

    def averageif(self,

                  output_cell,

                  range_cells,

                  criteria,

                  avg_range):

        self.sheet[output_cell] = (

            f'=AVERAGEIF({range_cells},"{criteria}",{avg_range})'

        )

        self.report.append(f"AVERAGEIF -> {output_cell}")

    # -----------------------------
    # Text
    # -----------------------------

    def concatenate(self,

                    output_cell,

                    *cells):

        joined = "&".join(cells)

        self.sheet[output_cell] = f"={joined}"

        self.report.append(f"CONCAT -> {output_cell}")

    def left(self,

             output_cell,

             cell,

             number):

        self.sheet[output_cell] = f"=LEFT({cell},{number})"

        self.report.append(f"LEFT -> {output_cell}")

    def right(self,

              output_cell,

              cell,

              number):

        self.sheet[output_cell] = f"=RIGHT({cell},{number})"

        self.report.append(f"RIGHT -> {output_cell}")

    def mid(self,

            output_cell,

            cell,

            start,

            length):

        self.sheet[output_cell] = (

            f"=MID({cell},{start},{length})"

        )

        self.report.append(f"MID -> {output_cell}")

    def len(self,

            output_cell,

            cell):

        self.sheet[output_cell] = f"=LEN({cell})"

        self.report.append(f"LEN -> {output_cell}")

    # -----------------------------
    # Date
    # -----------------------------

    def today(self,

              output_cell):

        self.sheet[output_cell] = "=TODAY()"

        self.report.append(f"TODAY -> {output_cell}")

    def now(self,

            output_cell):

        self.sheet[output_cell] = "=NOW()"

        self.report.append(f"NOW -> {output_cell}")

    def networkdays(self,

                    output_cell,

                    start,

                    end):

        self.sheet[output_cell] = (

            f"=NETWORKDAYS({start},{end})"

        )

        self.report.append(f"NETWORKDAYS -> {output_cell}")

    # -----------------------------
    # Save
    # -----------------------------

    def save(self):

        self.workbook.save(self.workbook_path)

    def get_report(self):

        return self.report