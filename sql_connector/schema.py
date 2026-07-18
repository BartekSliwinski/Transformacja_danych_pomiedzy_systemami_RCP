def create_departments_table(connection):
    create_departments_query = text(
        """
        IF OBJECT_ID('dbo.Departments', 'U') IS NULL
        BEGIN
            CREATE TABLE dbo.Departments (
                DepartmentID INT IDENTITY(1,1) PRIMARY KEY,
                DepartmentName VARCHAR(30) NOT NULL UNIQUE
            );
        END
        """
    )
    connection.execute(create_departments_query)
    connection.commit()