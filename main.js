/**
 * Type: Micro Service
 * Description: A short-lived service which is expected to complete within a fixed period of time.
 * @param {CbServer.BasicReq} req
 * @param {string} req.systemKey
 * @param {string} req.systemSecret
 * @param {string} req.userEmail
 * @param {string} req.userid
 * @param {string} req.userToken
 * @param {boolean} req.isLogging
 * @param {[id: string]} req.params
 * @param {CbServer.Resp} resp
 */

function first(req,resp){
    // These are parameters passed into the code service
    var params = req.params;
    // getting the payload from the params
    var body = params.body
    log(body)

    // replacing the ' with ". So that we can parse in json
    body = body.split("'").join('"')
    
    // parsing the payload to json 
    var x = JSON.parse(body)
    
    // making an object to save in db
    var data = {
        "cpu_info": x.cpu_info,
        "vmemory_info": x.vmemory_info,
    }

    var callback = function (err, data) {
        if (err) {
            log("Error:" + err.message);
        	resp.error("creation error : " + JSON.stringify(data));
        } else {
            log("Done");
        	resp.success("Done"+data);
        }
    };

    // initialising the api
    ClearBlade.init({request:req})
    // getting the collection refernce
    var col = ClearBlade.Collection({ collectionName: "preet_data" } );
    // saving the data
    // Change: from @var newPerson to @var data. Before I gave a wrong var.
    col.create(data, callback);
    // Change: Remove resp from here send the resp from callback only 
    // resp.success("GOOD");
}
