def parts_produced(elapsed_seconds: float, cycle_time_seconds: float) -> int:
    """
    Calculate the number of parts produced based on elapsed time and cycle time.

    Args:
        elapsed_seconds (float): The total elapsed time in seconds.
        cycle_time_seconds (float): The time taken to produce one part in seconds.

    Returns:
        int: The total number of parts produced.
    """
    if elapsed_seconds < 0:
        raise ValueError("Elapsed time cannot be negative.")
    if cycle_time_seconds <= 0:
        raise ValueError("Cycle time must be greater than zero.")
    
    return int(elapsed_seconds // cycle_time_seconds)