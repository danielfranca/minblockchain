import argparse
import httpserver


# TODO: Query latest block
# TODO: Traverse blocks until genesis
# TODO: Create bootnodes to connect
# TODO: Discovery other peers
# TODO: Improve formatting of message passing over TCP


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", help="Port to listen (default to 9999)")
    parser.add_argument("-t", "--http-port", help="HTTP Port to listen for commands (default to 8080)")

    parser.parse_args()

    port = parser.__dict__.get('port', 8080)

    httpserver.run_http_server(port)
