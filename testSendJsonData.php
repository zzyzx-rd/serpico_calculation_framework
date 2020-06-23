<?php
$request_url  = 'http://127.0.0.1:5000/main/criteriaComputation';
$curl = curl_init( $request_url );
// $myarray = array('postVar1key' => 'postVar1Data');
// // Setup request to send json via POST.
// $send_data = json_encode($myarray);
$send_data =
"{
    \"userWeights\": {
      \"1\": 100,
      \"2\": 200,
      \"3\": 300,
      \"4\": 400,
      \"5\": 500,
      \"6\": 600,
      \"7\": 700,
      \"8\": 800,
      \"9\": 900,
      \"10\": 1000,
      \"11\": 1100
    },
    \"teams\": {
      \"1\": [\"1\", \"3\", \"5\", \"7\"],
      \"2\": [\"2\",\"4\", \"8\"],
      \"3\": [\"6\", \"9\"]
    },
    \"teamWeights\": {
      \"1\": 1600,
      \"2\": 1400,
      \"3\": 1500
    },
    \"criterias\": {
        \"crit1\": {
            \"lowerBound\": 1,
            \"upperBound\": 20,
            \"userGrades\": {
                \"1\": {
                    \"3\": 5,
                    \"5\": 7,
                    \"7\": 11,
                    \"10\": 10
                },
                \"2\": {
                    \"4\": 6,
                    \"8\": 16
                },
                \"3\": {
                    \"3\": 20,
                    \"7\": 14
                },
                \"4\":{
                    \"4\": 18,
                    \"10\": 16
                },
                \"5\": {
                    \"5\": 17,
                    \"7\": 8
                },
                \"6\": {
                    \"6\": 6,
                    \"9\": 4,
                    \"10\": 5
                },
                \"10\": {
                    \"10\": 19
                }
            },
            \"teamGrades\": {
                \"1\": {
                    \"2\": 8,
                    \"3\": 7
                },
                \"2\": {
                    \"3\": 16
                },
                \"3\": {
                    \"2\": 7
                },
                \"4\": {
                    \"1\": 12,
                    \"3\": 16
                },
                \"5\": {
                    \"2\": 6
                },
                \"6\": {
                    \"1\": 13,
                    \"2\": 15
                }
            }
        },
        \"crit2\": {
            \"lowerBound\": 1,
            \"upperBound\": 20,
            \"userGrades\": {
                \"1\": {
                    \"3\": 5,
                    \"5\": 7,
                    \"7\": 11,
                    \"10\": 10
                },
                \"2\": {
                    \"4\": 6,
                    \"8\": 16
                },
                \"3\": {
                    \"3\": 20,
                    \"7\": 14
                },
                \"4\":{
                    \"4\": 18,
                    \"10\": 16
                },
                \"5\": {
                    \"5\": 17,
                    \"7\": 8
                },
                \"6\": {
                    \"6\": 6,
                    \"9\": 4,
                    \"10\": 5
                },
                \"10\": {
                    \"10\": 19
                }
            },
            \"teamGrades\": {
                \"1\": {
                    \"2\": 8,
                    \"3\": 7
                },
                \"2\": {
                    \"3\": 16
                },
                \"3\": {
                    \"2\": 7
                },
                \"4\": {
                    \"1\": 12,
                    \"3\": 16
                },
                \"5\": {
                    \"2\": 6
                },
                \"6\": {
                    \"1\": 13,
                    \"2\": 15
                }
            }
        }
    }
}";
curl_setopt( $curl, CURLOPT_POSTFIELDS, $send_data );
curl_setopt( $curl, CURLOPT_HTTPHEADER, array('Content-Type:application/json'));
# Return response instead of printing.
curl_setopt( $curl, CURLOPT_RETURNTRANSFER, true );
# Send request.
$result = curl_exec($curl);
curl_close($curl);
# Print response.
print("it should append something");
echo "<pre>$result</pre>";

$request_url  = 'http://127.0.0.1:5000/main/stageComputation';
$curl = curl_init( $request_url );
$send_data = "{
    \"user\":[\"1\", \"2\", \"3\", \"4\", \"5\", \"6\", \"7\", \"8\", \"9\", \"10\"],
    \"team\":[\"1\", \"2\", \"3\"],
    \"crit1\":{
        \"weight\": 60,
        \"averageUsersWeightedResult\": 2,
        \"averageUsersEqualResult\": 2,
        \"averageTeamsWeightedResult\": 2,
        \"averageTeamsEqualResult\": 2,
        \"averageUsersWeightedRelativeResult\": 2,
        \"averageUsersEqualRelativeResult\": 2,
        \"averageTeamsWeightedRelativeResult\": 2,
        \"averageTeamsEqualRelativeResult\": 2,
        \"averageUsersWeightedStdDev\": 2,
        \"averageUsersEqualStdDev\": 2,
        \"averageTeamsWeightedStdDev\": 2,
        \"averageTeamsEqualStdDev\": 2,
        \"maxUsersWeightedStdDev\": 2,
        \"maxUsersEqualStdDev\": 2,
        \"maxTeamsWeightedStdDev\": 2,
        \"maxTeamsEqualStdDev\": 2,
        \"weightedUserInertia\": 2,
        \"equalUserInertia\": 2,
        \"weightedTeamInertia\": 2,
        \"equalTeamInertia\": 2,
        \"maxWeightedUserInertia\": 2,
        \"maxEqualUserInertia\": 2,
        \"maxWeightedTeamInertia\": 2,
        \"maxEqualTeamInertia\": 2,
        \"weightedUserDevRatio\": 2,
        \"equalUserDevRatio\": 2,
        \"weightedTeamDevRatio\": 2,
        \"equalTeamDevRatio\": 2,
        \"user\": {
            \"3\": {
                \"weightedResult\": 2,
                \"equalResult\": 2,
                \"weightedRelativeResult\": 2,
                \"equalRelativeResult\": 2,
                \"weightedStdDev\": 2,
                \"equalStdDev\": 2,
                \"weightedDevRatio\": 2,
                \"equalDevRatio\": 2
            },
            \"4\": {
                \"weightedResult\": 2,
                \"equalResult\": 2,
                \"weightedRelativeResult\": 2,
                \"equalRelativeResult\": 2,
                \"weightedStdDev\": 2,
                \"equalStdDev\": 2,
                \"weightedDevRatio\": 2,
                \"equalDevRatio\": 2
            },
            \"5\": {
                \"weightedResult\": 2,
                \"equalResult\": 2,
                \"weightedRelativeResult\": 2,
                \"equalRelativeResult\": 2,
                \"weightedStdDev\": 2,
                \"equalStdDev\": 2,
                \"weightedDevRatio\": 2,
                \"equalDevRatio\": 2
            },
            \"6\": {
                \"weightedResult\": 2,
                \"equalResult\": 2,
                \"weightedRelativeResult\": 2,
                \"equalRelativeResult\": 2,
                \"weightedStdDev\": 2,
                \"equalStdDev\": 2,
                \"weightedDevRatio\": 2,
                \"equalDevRatio\": 2
            },
            \"7\": {
                \"weightedResult\": 2,
                \"equalResult\": 2,
                \"weightedRelativeResult\": 2,
                \"equalRelativeResult\": 2
            },
            \"8\": {
                \"weightedResult\": 2,
                \"equalResult\": 2,
                \"weightedRelativeResult\": 2,
                \"equalRelativeResult\": 2
            },
            \"9\": {
                \"weightedResult\": 2,
                \"equalResult\": 2,
                \"weightedRelativeResult\": 2,
                \"equalRelativeResult\": 2
            },
            \"10\": {
                \"weightedResult\": 2,
                \"equalResult\": 2,
                \"weightedRelativeResult\": 2,
                \"equalRelativeResult\": 2,
                \"weightedStdDev\": 2,
                \"equalStdDev\": 2,
                \"weightedDevRatio\": 2,
                \"equalDevRatio\": 2
            },
            \"1\": {
                \"weightedStdDev\": 2,
                \"equalStdDev\": 2,
                \"weightedDevRatio\": 2,
                \"equalDevRatio\": 2
            },
            \"2\": {
                \"weightedStdDev\": 2,
                \"equalStdDev\": 2,
                \"weightedDevRatio\": 2,
                \"equalDevRatio\": 2
            }
      },
      \"team\": {
          \"1\": {
              \"weightedResult\": 2,
              \"equalResult\": 2,
              \"weightedRelativeResult\": 2,
              \"equalRelativeResult\": 2,
              \"weightedStdDev\": 2,
              \"equalStdDev\": 2,
              \"weightedDevRatio\": 2,
              \"equalDevRatio\": 2
          },
          \"2\": {
              \"weightedResult\": 2,
              \"equalResult\": 2,
              \"weightedRelativeResult\": 2,
              \"equalRelativeResult\": 2,
              \"weightedStdDev\": 2,
              \"equalStdDev\": 2,
              \"weightedDevRatio\": 2,
              \"equalDevRatio\": 2
          },
          \"3\": {
              \"weightedResult\": 2,
              \"equalResult\": 2,
              \"weightedRelativeResult\": 2,
              \"equalRelativeResult\": 2,
              \"weightedStdDev\": 2,
              \"equalStdDev\": 2,
              \"weightedDevRatio\": 2,
              \"equalDevRatio\": 2
          }
      }
      },
    \"crit2\":{
        \"weight\": 40,
        \"averageUsersWeightedResult\": 3,
        \"averageUsersEqualResult\": 3,
        \"averageTeamsWeightedResult\": 3,
        \"averageTeamsEqualResult\": 3,
        \"averageUsersWeightedRelativeResult\": 3,
        \"averageUsersEqualRelativeResult\": 3,
        \"averageTeamsWeightedRelativeResult\": 3,
        \"averageTeamsEqualRelativeResult\": 3,
        \"averageUsersWeightedStdDev\": 3,
        \"averageUsersEqualStdDev\": 3,
        \"averageTeamsWeightedStdDev\": 3,
        \"averageTeamsEqualStdDev\": 3,
        \"maxUsersWeightedStdDev\": 3,
        \"maxUsersEqualStdDev\": 3,
        \"maxTeamsWeightedStdDev\": 3,
        \"maxTeamsEqualStdDev\": 3,
        \"weightedUserInertia\": 3,
        \"equalUserInertia\": 3,
        \"weightedTeamInertia\": 3,
        \"equalTeamInertia\": 3,
        \"maxWeightedUserInertia\": 3,
        \"maxEqualUserInertia\": 3,
        \"maxWeightedTeamInertia\": 3,
        \"maxEqualTeamInertia\": 3,
        \"weightedUserDevRatio\": 3,
        \"equalUserDevRatio\": 3,
        \"weightedTeamDevRatio\": 3,
        \"equalTeamDevRatio\": 3,
        \"user\": {
            \"3\": {
                \"weightedResult\": 3,
                \"equalResult\": 3,
                \"weightedRelativeResult\": 3,
                \"equalRelativeResult\": 3,
                \"weightedStdDev\": 3,
                \"equalStdDev\": 3,
                \"weightedDevRatio\": 3,
                \"equalDevRatio\": 3
            },
            \"4\": {
                \"weightedResult\": 3,
                \"equalResult\": 3,
                \"weightedRelativeResult\": 3,
                \"equalRelativeResult\": 3,
                \"weightedStdDev\": 3,
                \"equalStdDev\": 3,
                \"weightedDevRatio\": 3,
                \"equalDevRatio\": 3
            },
            \"5\": {
                \"weightedResult\": 3,
                \"equalResult\": 3,
                \"weightedRelativeResult\": 3,
                \"equalRelativeResult\": 3,
                \"weightedStdDev\": 3,
                \"equalStdDev\": 3,
                \"weightedDevRatio\": 3,
                \"equalDevRatio\": 3
            },
            \"6\": {
                \"weightedResult\": 3,
                \"equalResult\": 3,
                \"weightedRelativeResult\": 3,
                \"equalRelativeResult\": 3,
                \"weightedStdDev\": 3,
                \"equalStdDev\": 3,
                \"weightedDevRatio\": 3,
                \"equalDevRatio\": 3
            },
            \"7\": {
                \"weightedResult\": 3,
                \"equalResult\": 3,
                \"weightedRelativeResult\": 3,
                \"equalRelativeResult\": 3
            },
            \"8\": {
                \"weightedResult\": 3,
                \"equalResult\": 3,
                \"weightedRelativeResult\": 3,
                \"equalRelativeResult\": 3
            },
            \"9\": {
                \"weightedResult\": 3,
                \"equalResult\": 3,
                \"weightedRelativeResult\": 3,
                \"equalRelativeResult\": 3
            },
            \"10\": {
                \"weightedResult\": 3,
                \"equalResult\": 3,
                \"weightedRelativeResult\": 3,
                \"equalRelativeResult\": 3,
                \"weightedStdDev\": 3,
                \"equalStdDev\": 3,
                \"weightedDevRatio\": 3,
                \"equalDevRatio\": 3
            },
            \"1\": {
                \"weightedStdDev\": 3,
                \"equalStdDev\": 3,
                \"weightedDevRatio\": 3,
                \"equalDevRatio\": 3
            },
            \"2\": {
                \"weightedStdDev\": 3,
                \"equalStdDev\": 3,
                \"weightedDevRatio\": 3,
                \"equalDevRatio\": 3
            }
      },
      \"team\": {
          \"1\": {
              \"weightedResult\": 3,
              \"equalResult\": 3,
              \"weightedRelativeResult\": 3,
              \"equalRelativeResult\": 3,
              \"weightedStdDev\": 3,
              \"equalStdDev\": 3,
              \"weightedDevRatio\": 3,
              \"equalDevRatio\": 3
          },
          \"2\": {
              \"weightedResult\": 3,
              \"equalResult\": 3,
              \"weightedRelativeResult\": 3,
              \"equalRelativeResult\": 3,
              \"weightedStdDev\": 3,
              \"equalStdDev\": 3,
              \"weightedDevRatio\": 3,
              \"equalDevRatio\": 3
          },
          \"3\": {
              \"weightedResult\": 3,
              \"equalResult\": 3,
              \"weightedRelativeResult\": 3,
              \"equalRelativeResult\": 3,
              \"weightedStdDev\": 3,
              \"equalStdDev\": 3,
              \"weightedDevRatio\": 3,
              \"equalDevRatio\": 2
          }
      }
      }
  }";

  curl_setopt( $curl, CURLOPT_POSTFIELDS, $send_data );
  curl_setopt( $curl, CURLOPT_HTTPHEADER, array('Content-Type:application/json'));
  # Return response instead of printing.
  curl_setopt( $curl, CURLOPT_RETURNTRANSFER, true );
  # Send request.
  $result = curl_exec($curl);
  curl_close($curl);
  # Print response.
  print("it should append something");
  echo "<pre>$result</pre>";
