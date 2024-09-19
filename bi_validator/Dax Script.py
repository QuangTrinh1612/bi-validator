Test_Page_Overview = f'''
// DAX Query
DEFINE
	VAR __DS0FilterTable = 
		TREATAS({"E"}, 'Dim - Employee Type'[EMPLOYEE_TYPE])

	VAR __DS0Core = 
		CALCULATETABLE(
			SUMMARIZE(
				'Dim - Employee Type',
				'Dim - Employee Type'[EMPLOYEE_TYPE],
				'Dim - Employee Type'[EMPLOYEE_TYPE_PK]
			),
			KEEPFILTERS(__DS0FilterTable)
		)

	VAR __DS0PrimaryWindowed = 
		TOPN(
			501,
			__DS0Core,
			'Dim - Employee Type'[EMPLOYEE_TYPE_PK],
			1,
			'Dim - Employee Type'[EMPLOYEE_TYPE],
			1
		)

EVALUATE
	__DS0PrimaryWindowed

ORDER BY
	'Dim - Employee Type'[EMPLOYEE_TYPE_PK], 'Dim - Employee Type'[EMPLOYEE_TYPE]
'''