(*
 * 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without 
 * any remainder.

 * What is the smallest positive number that is evenly divisible by all of the numbers from 1 
 * to 20?
*)

let rec checkDivis (n, divis) =
	if divis == 20 then (n, 1) else
		(if n mod divis == 0 then checkDivis(n, divis + 1) else (n, 0))

let rec findSmallest n =
	let (smallest, check) = checkDivis (n, 2) in
		if check == 1 then smallest else findSmallest n + 1
