from googleapiclient import discovery
import argparse
import json



if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("--api_key", type=str, required=True,
                        help="API Key for Perspective API, see https://support.perspectiveapi.com/s/docs-get-started")
  
  args = parser.parse_args()
  print(f"Parameters: {args}")
  client = discovery.build(
    "commentanalyzer",
    "v1alpha1",
    developerKey=args.api_key,
    discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
    static_discovery=False,
  )

  analyze_request = {
    'comment': { 'text': 'I hate my friend damon' },
    'requestedAttributes': {'TOXICITY': {}}
  }

  response = client.comments().analyze(body=analyze_request).execute()
  print(json.dumps(response, indent=2))