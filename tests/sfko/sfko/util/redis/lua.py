local current_epoch=redis.call("GET", "current-epoch")
if current_epoch == ARGV[1] then
	redis.call('RPUSH', 'tasks', ARGV[2])
	return true
else
	return nil
end


-- Roll EPOCH
-- pass epoch key, current epoch, new epoch
-- always succeeds if there isn't an epoch set
local epoch_key = KEYS[1]
local current_epoch = redis.call("GET", epoch_key)
if current_epoch == nil or current_epoch == ARGV[1] then
	redis.call("SET", epoch_key, ARGV[2])
	return ARGV[2]
end
return current_epoch


--Protected Add
--Adds EPOCH info to queue elements for checing on retrieval
local epoch_key = KEYS[1]
local task_key = KEYS[2]
local current_epoch = redis.call("GET", epoch_key)
return redis.call("RPUSH", task_key, { current_epoch, ARGV[1] })

--Protected Pop
--Pops a queue element comparing epochs
local epoch_key = KEYS[1]
local task_key = KEYS[2]
local current_epoch = redis.call("GET", epoch_key)
repeat
	local task = redis.call("LPOP", task_key)
until task == nil or task[1] == current
if task == nil
	return nil
return task[2]
