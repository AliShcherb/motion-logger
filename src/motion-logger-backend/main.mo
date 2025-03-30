import Nat "mo:base/Nat";
import Text "mo:base/Text";
import Array "mo:base/Array";

actor MotionLogger {

  type Event = {
    state: Text;
    time: Text;
  };

  var events : [Event] = [];

  public shared func log_event(state: Text, time: Text) : async Text {
    let event : Event = { state = state; time = time };
    events := Array.append<Event>(events, [event]);
    return "Event logged: " # state # " at " # time;
  };

  public query func get_events() : async [Event] {
    return events;
  };
}

