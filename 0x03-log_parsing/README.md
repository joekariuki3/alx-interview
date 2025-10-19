# Log Parsing

Read from stdin, parse log lines, and print running metrics.

### Expected input format

`<IP> - [<date>] "GET /projects/260 HTTP/1.1" <status_code> <file_size>`

### Output

- Every 10 lines and on interrupt: print
  - `File size: <total_size>`
  - Each status code count in ascending order

### Usage

```bash
python3 0-generator.py | python3 0-stats.py
```
