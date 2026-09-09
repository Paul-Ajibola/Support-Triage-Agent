# to manage external program
import subprocess
# to create temporary files and directories
import tempfile
#  to interact with os
import os


def sandbox_runner(code: str, timeout: int=5) -> dict:
    """Execute a bug-report code snippet in an isolated Docker container."""
    # create temporty file with a name
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
        # don't delete because we'll hand it down to docker later. We'll delete later ourselves
        f.write(code)
        # get the temp file location (path)
        script_path = f.name

    try:
        result = subprocess.run(
            [
                "docker", "run", "--rm",
                "--network", "none",
                "-v", f"{script_path}:/sandbox/script.py:ro",
                "python:3.11-slim",
                "python", "/sandbox/script.py"
            ],
            capture_output=True,
            text=True,
            timeout=timeout
        )


        return {"stdout": result.stdout, "stderr": result.stderr, "exit_code": result.returncode}
    except subprocess.TimeoutExpired:
        return {"stdout": "", "stderr": "Execution timed out", "exit_code": -1}
    # finally -> execute code irrespective of what happens above
    finally:
        os.remove(script_path)

# ro -> read-only

