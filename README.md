# Error Visor

## Que es?
Es un proyecto destinado a guardar registros personalizados en un archivo json que será utilizado
más tarde para visualizarse en una app web de forma localizada y ordenada. Solo es necesaria una
sentencia y listo, ya tienes el registro del error en tu app.

## Cómo funciona?

Primero instalamos con:

```bash
pip install error-visor
```

Importamos el módulo:

```python
import error_visor as EV
```

Luego localizamos el lugar desde donde queremos mandar el log. Por ejemplo un bloque `exception` y
colocamos el siguiente código:

```python
except Exception as ex:

	EV.Logger.err(
		EV.Error(
			description='Error de muestra',
			ex=ex,
			priority=EV.Priority.HIGH
		)
	)

```

Para una `advertencia`/`warning`:

```python
except Exception as ex:

	EV.Logger.warn(
		EV.Warning(
			description='Advertencia de muestra',
			ex=ex,
      		follow_me=True
		)
	)

```

Y listo, tendremos el registro en un json!


## CHANGELOG

### v0.0.3
- Fixed: Making of new `logs` dir when that not exists. Really work now!
- Added: Warning Type
- Modified: RTypes have have new format to use. RTypes are like: `EV.Error`, `EV.Warning`, etc.

### v0.0.2
- Fixed: Making of new `logs` dir when that not exists

### v0.0.1
- First upload
