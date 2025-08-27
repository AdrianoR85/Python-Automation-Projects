CREATE OR REPLACE FUNCTION log_employee_changes()
RETURNS TRIGGER 
SECURITY DEFINER AS
$body$
BEGIN
	IF TG_OP = 'DELETE' THEN
		INSERT INTO employee_audit (
			employee_id, name, phone, role, gender, salary, operation_type, changed_by
		)
		VALUES (OLD.id, OLD.name, OLD.phone, OLD.role, OLD.gender, OLD.salary,TG_OP, SESSION_USER);
		RETURN OLD;
	ELSIF TG_OP = 'UPDATE' THEN
		INSERT INTO employee_audit (
			employee_id, name, phone, role, gender, salary, operation_type,changed_by
		)
		VALUES (OLD.id, OLD.name, OLD.phone, OLD.role, OLD.gender, OLD.salary,TG_OP, SESSION_USER);
		RETURN NEW;
	END IF;
END;
$body$
LANGUAGE plpgsql;

CREATE TRIGGER tg_employee_audit
AFTER UPDATE OR DELETE ON employee
FOR EACH ROW
EXECUTE FUNCTION log_employee_changes();