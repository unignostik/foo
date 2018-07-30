CREATE PROCEDURE updateAPA (IN company VARCHAR(100), IN firstName VARCHAR(100), IN lastName VARCHAR(100), IN email VARCHAR(100)
LANGUAGE SQL
P1: BEGIN

SET LEFT(SUBSTRING(Result, (CHARINDEX(‘caFirstname’,Result, 0)+14, 20), LEN(SUBSTRING(Result, (CHARINDEX(‘caFirstname’,Result, 0)+14, 20)-1) = firstName;
SET LEFT(SUBSTRING(Result, (CHARINDEX(‘caLastname’,Result, 0)+14, 20), LEN(SUBSTRING(Result, (CHARINDEX(‘caLastname’,Result, 0)+14, 20)-1) = lastName;
SET LEFT(SUBSTRING(Result, (CHARINDEX(‘caEmail’,Result, 0)+14, 20), LEN(SUBSTRING(Result, (CHARINDEX(‘caEmail’,Result, 0)+14, 20)-1) = email;
                                                                        
FROM db2_audit
WHERE CompanyName = company
                                                                        
END P1                                                                       
                            
