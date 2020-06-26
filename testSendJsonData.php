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

    },
    \"teamWeights\": {

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
#print("it should append something");
print_r($result);

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

  $send_data = "{\"user\": [298, 284], \"team\": [], \"821\": {\"averageUsersWeightedResult\": 2.5, \"averageUsersEqualResult\": 2.5, \"averageTeamsWeightedResult\": 0, \"averageTeamsEqualResult\": 0, \"averageUsersWeightedRelativeResult\": 0.5, \"averageUsersEqualRelativeResult\": 0.5, \"averageTeamsWeightedRelativeResult\": 0, \"averageTeamsEqualRelativeResult\": 0, \"averageUsersWeightedStdDev\": 0, \"averageUsersEqualStdDev\": 0, \"averageTeamsWeightedStdDev\": 0, \"averageTeamsEqualStdDev\": 0, \"maxUsersWeightedStdDev\": 3, \"maxUsersEqualStdDev\": 3, \"maxTeamsWeightedStdDev\": 0, \"maxTeamsEqualStdDev\": 0, \"weightedUserInertia\": 0, \"equalUserInertia\": 0, \"weightedTeamInertia\": 0, \"equalTeamInertia\": 0, \"maxWeightedUserInertia\": 9, \"maxEqualUserInertia\": 9, \"maxWeightedTeamInertia\": 0, \"maxEqualTeamInertia\": 0, \"weightedUserDevRatio\": 0, \"equalUserDevRatio\": 0, \"weightedTeamDevRatio\": 0, \"equalTeamDevRatio\": 0, \"user\": {\"298\": {\"weightedResult\": 2, \"equalResult\": 2, \"weightedRelativeResult\": 0.4, \"equalRelativeResult\": 0.4}, \"284\": {\"weightedResult\": 3, \"equalResult\": 3, \"weightedRelativeResult\": 0.6, \"equalRelativeResult\": 0.6, \"weightedStdDev\": 0, \"equalStdDev\": 0, \"weightedDevRatio\": 0, \"equalDevRatio\": 0}}, \"team\": [], \"weight\": 0.7}, \"822\": {\"averageUsersWeightedResult\": 4.5, \"averageUsersEqualResult\": 4.5, \"averageTeamsWeightedResult\": 0, \"averageTeamsEqualResult\": 0, \"averageUsersWeightedRelativeResult\": 0.9, \"averageUsersEqualRelativeResult\": 0.9, \"averageTeamsWeightedRelativeResult\": 0, \"averageTeamsEqualRelativeResult\": 0, \"averageUsersWeightedStdDev\": 0, \"averageUsersEqualStdDev\": 0, \"averageTeamsWeightedStdDev\": 0, \"averageTeamsEqualStdDev\": 0, \"maxUsersWeightedStdDev\": 4.53, \"maxUsersEqualStdDev\": 4.53, \"maxTeamsWeightedStdDev\": 0, \"maxTeamsEqualStdDev\": 0, \"weightedUserInertia\": 0, \"equalUserInertia\": 0, \"weightedTeamInertia\": 0, \"equalTeamInertia\": 0, \"maxWeightedUserInertia\": 20.5, \"maxEqualUserInertia\": 20.5, \"maxWeightedTeamInertia\": 0, \"maxEqualTeamInertia\": 0, \"weightedUserDevRatio\": 0, \"equalUserDevRatio\": 0, \"weightedTeamDevRatio\": 0, \"equalTeamDevRatio\": 0, \"user\": {\"298\": {\"weightedResult\": 4, \"equalResult\": 4, \"weightedRelativeResult\": 0.8, \"equalRelativeResult\": 0.8}, \"284\": {\"weightedResult\": 5, \"equalResult\": 5, \"weightedRelativeResult\": 1, \"equalRelativeResult\": 1, \"weightedStdDev\": 0, \"equalStdDev\": 0, \"weightedDevRatio\": 0, \"equalDevRatio\": 0}}, \"team\": [], \"weight\": 0.3}}";

  curl_setopt( $curl, CURLOPT_POSTFIELDS, $send_data );
  curl_setopt( $curl, CURLOPT_HTTPHEADER, array('Content-Type:application/json'));
  # Return response instead of printing.
  curl_setopt( $curl, CURLOPT_RETURNTRANSFER, true );
  # Send request.
  $result = curl_exec($curl);
  curl_close($curl);
# Print response.
$json = '{"a":1,"b":2,"c":3,"d":4,"e":5}';
$json = json_decode($json);
print_r($json);
  #print($result);
  $resultA = json_decode($result, true);
//   echo "\nResult : ";
  print_r($resultA);
  foreach ($resultA as $key => $value) {
    echo "key : ";  
    echo $key ;
      echo "\n  value : ";
    //   print_r($value);
      echo gettype($value);
      #echo "\n  ";
      foreach ($value as $key2 => $value2) {
        echo $key2 ;
        echo "\n    ";
        echo gettype($value2);
        echo "\n ";
        // echo $resultA[$key];
        #echo "\n";      
      }
      echo "\n";
  }
  #echo $resultA['crit1']["user"];
