CREATE TABLE employe (
	id SERIAL PRIMARY KEY,
	name VARCHAR(100) UNIQUE NOT NULL,
	phone VARCHAR(20) NOT NULL,
	role VARCHAR(50) NOT NULL, 	
	gender VARCHARR(10) NOT NULL,
	salary NUMERIC(10,2) NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)

-- This table will be used to record the data that was deleted or updated 
CREATE TABLE employee_audit (
    audit_id SERIAL PRIMARY KEY,
    employee_id INT,
    name VARCHAR(100),
    phone VARCHAR(20),
    role VARCHAR(50),
    gender VARCHAR(10),
    salary NUMERIC(10,2),
    operation_type VARCHAR(10) NOT NULL, -- 'UPDATE' ou 'DELETE'
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    changed_by TEXT DEFAULT current_user -- opcional, se quiser guardar o usuário do banco
);