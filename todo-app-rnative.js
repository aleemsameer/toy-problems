import React from 'react';
import { Text, TextInput, Button, View} from 'react-native';
import DatePicker from 'react-native-datepicker';

function Task(props) {
  return <View style={{ flexDirection: "row" }}>
    <Text> {props.name}, {props.dueDate}</Text>
    <Button title="Delete" color="#ff8c00" onPress={props.onDeleteTask}>Delete</Button>
  </View >
}

export default class TodoList extends React.Component {
  constructor(props) {
    super(props);
    this.state = {list: []};
    this.handleAddTask = this.handleAddTask.bind(this);
    this.handleDeleteTask = this.handleDeleteTask.bind(this);
  }
  handleAddTask(task) {
    console.log("add task clicked");
    this.state.list.push(task);
    this.setState({ list: this.state.list })
  }
  handleDeleteTask(task1) {
    console.log("delete task clicked");
    this.setState({ list: this.state.list.filter(task => task.id != task1) })
  }
  render() {
    return (
      <View style={{ justifyContent: 'center', alignItems: 'center'}} >
        <Text style={{color: "#00008b", fontSize: 50}}>ToDo List</Text>
        <TaskNameForm onAddTask={this.handleAddTask}/>
        <View style={{paddingTop: 25, fontSize: 25}}>
        {
          this.state.list.map((t) =>
            <Task key={t.id} name={t.name} dueDate={t.dueDate} id= {t.id} 
            onDeleteTask= {() => this.handleDeleteTask(t.id)}/>)
        }
        </View>
      </View >
    );
  }
}

class TaskNameForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = { value: '', date: '' };

    this.handleDateChange = this.handleDateChange.bind(this);
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleSubmit(event) {
    const taskList = this.props.taskList;
    // create a task objec
    event.preventDefault();
    const task={id: Date.now(), name: this.state.value, 
    dueDate: this.state.date
    };
    // add the task object to the task list
    this.props.onAddTask(task);
    this.setState({ value: '', date: '' })
  }

  handleChange = (text) => {
    // code to set the state of the component
    this.setState({ value: text })
  }
  handleDateChange = (date) => {
    // code to set the date
    this.setState({ date: date })
  }

  render() {
    return (
      <View style={{ paddingTop: 25, fontSize: 25}}>
        <View style={{ flexDirection: "row" }}>
          <TextInput type="text" value={this.state.value} style={{ fontSize: 20} }
          placeholder="Enter task " onChangeText={this.handleChange}/>
          <DatePicker mode="date" format="DD-MM-YYYY" date={this.state.date} 
          onDateChange={this.handleDateChange}/>
          <Button type="submit" title="Add Task" color="green" onPress={this.handleSubmit}/>
        </View>
      </View >
    );
  }
}